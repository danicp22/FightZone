from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = "fightzone_clave_secreta_2026"

# ══════════════════════════════════════════════════════
#  BASE DE DATOS
# ══════════════════════════════════════════════════════

DB_CONFIG = {
    "host":     "mysql.railway.internal",
    "database": "railway",
    "user":     "root",
    "password": "gPTRzuSfplxbJIRdtpTrmjjCNdybJLNn"
}

def conectar():
    return mysql.connector.connect(**DB_CONFIG)


# ══════════════════════════════════════════════════════
#  DECORADORES
# ══════════════════════════════════════════════════════

def login_requerido(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "usuario_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper

def admin_requerido(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if session.get("rol") != "admin":
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return wrapper


# ══════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════

def get_cart_count():
    if "usuario_id" not in session:
        return 0
    try:
        con = conectar()
        cur = con.cursor(dictionary=True)
        cur.execute("""
            SELECT COALESCE(SUM(ci.cantidad), 0) AS total
            FROM carrito c
            JOIN carrito_items ci ON ci.carrito_id = c.id
            WHERE c.usuario_id = %s
        """, (session["usuario_id"],))
        row = cur.fetchone()
        con.close()
        return int(row["total"]) if row else 0
    except:
        return 0

def get_or_create_carrito(usuario_id):
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT id FROM carrito WHERE usuario_id = %s", (usuario_id,))
    row = cur.fetchone()
    if row:
        carrito_id = row["id"]
    else:
        cur.execute("INSERT INTO carrito (usuario_id) VALUES (%s)", (usuario_id,))
        con.commit()
        carrito_id = cur.lastrowid
    con.close()
    return carrito_id


# ══════════════════════════════════════════════════════
#  ARREGLO INICIAL: hashear password del admin si es texto plano
#  (el INSERT del SQL mete 'Admin123!' sin hashear)
# ══════════════════════════════════════════════════════

def fix_admin_password():
    try:
        con = conectar()
        cur = con.cursor(dictionary=True)
        cur.execute("SELECT id, password FROM usuarios WHERE email = 'admin@fightzone.com'")
        admin = cur.fetchone()
        if admin:
            pwd = admin["password"]
            # Si NO empieza por pbkdf2/scrypt/bcrypt, está en texto plano → hashear
            if not pwd.startswith(("pbkdf2:", "scrypt:", "$2b$", "$2a$")):
                hashed = generate_password_hash(pwd)
                cur.execute("UPDATE usuarios SET password = %s WHERE id = %s",
                            (hashed, admin["id"]))
                con.commit()
        con.close()
    except Exception as e:
        print(f"[fix_admin_password] {e}")

fix_admin_password()


# ══════════════════════════════════════════════════════
#  PÁGINAS
# ══════════════════════════════════════════════════════

@app.route("/")
def index():
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("""
        SELECT p.*, c.nombre AS categoria_nombre
        FROM productos p
        LEFT JOIN categorias c ON p.categoria_id = c.id
        ORDER BY p.fecha_creacion DESC
        LIMIT 8
    """)
    productos = cur.fetchall()
    con.close()
    return render_template("index.html",
                           productos=productos,
                           cart_count=get_cart_count(),
                           usuario=session.get("usuario_nombre"))


@app.route("/productos")
def productos():
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM categorias ORDER BY nombre")
    categorias = cur.fetchall()
    con.close()
    return render_template("productos.html",
                           categorias=categorias,
                           cart_count=get_cart_count(),
                           usuario=session.get("usuario_nombre"))


@app.route("/producto/<int:id>")
def producto(id):
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("""
        SELECT p.*, c.nombre AS categoria_nombre
        FROM productos p
        LEFT JOIN categorias c ON p.categoria_id = c.id
        WHERE p.id = %s
    """, (id,))
    p = cur.fetchone()
    con.close()
    if not p:
        return redirect(url_for("productos"))
    return render_template("producto.html",
                           producto=p,
                           cart_count=get_cart_count(),
                           usuario=session.get("usuario_nombre"))


@app.route("/quienes-somos")
def quienes_somos():
    return render_template("informacion.html",
                           cart_count=get_cart_count(),
                           usuario=session.get("usuario_nombre"))


# ══════════════════════════════════════════════════════
#  AUTH
# ══════════════════════════════════════════════════════

@app.route("/registro")
def registro():
    if "usuario_id" in session:
        return redirect(url_for("index"))
    return render_template("registro.html")


@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    nombre   = request.form.get("nombre",   "").strip()
    email    = request.form.get("email",    "").strip()
    password = request.form.get("password", "")

    # El campo apellido es opcional (la BD no lo tiene)
    if not all([nombre, email, password]):
        return render_template("registro.html", error="Todos los campos son obligatorios.")

    hashed = generate_password_hash(password)
    con = conectar()
    cur = con.cursor()
    try:
        cur.execute(
            "INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)",
            (nombre, email, hashed)
        )
        con.commit()
        con.close()
        return redirect(url_for("login"))
    except mysql.connector.IntegrityError:
        con.close()
        return render_template("registro.html", error="Este email ya esta registrado.")


@app.route("/login")
def login():
    if "usuario_id" in session:
        return redirect(url_for("index"))
    return render_template("login.html")


@app.route("/login_usuario", methods=["POST"])
def login_usuario():
    email    = request.form.get("email",    "").strip()
    password = request.form.get("password", "")

    if not email or not password:
        return render_template("login.html", error="Introduce email y contrasena.")

    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    usuario = cur.fetchone()
    con.close()

    # Sin usuario encontrado
    if not usuario:
        return render_template("login.html", error="Email o contrasena incorrectos.")

    # Comprobar password
    if not check_password_hash(usuario["password"], password):
        return render_template("login.html", error="Email o contrasena incorrectos.")

    # Login correcto
    session["usuario_id"]     = usuario["id"]
    session["usuario_nombre"] = usuario["nombre"]
    session["rol"]            = usuario["rol"]

    if usuario["rol"] == "admin":
        return redirect(url_for("admin"))
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


# ══════════════════════════════════════════════════════
#  CARRITO
# ══════════════════════════════════════════════════════

@app.route("/carrito")
@login_requerido
def carrito():
    carrito_id = get_or_create_carrito(session["usuario_id"])
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("""
        SELECT ci.id AS item_id, ci.cantidad,
               p.id AS producto_id, p.nombre, p.precio, p.imagen,
               c.nombre AS categoria_nombre
        FROM carrito_items ci
        JOIN productos p ON ci.producto_id = p.id
        LEFT JOIN categorias c ON p.categoria_id = c.id
        WHERE ci.carrito_id = %s
    """, (carrito_id,))
    items = cur.fetchall()
    con.close()
    subtotal = sum(float(i["precio"]) * i["cantidad"] for i in items)
    return render_template("carrito.html",
                           items=items,
                           subtotal=subtotal,
                           cart_count=get_cart_count(),
                           usuario=session.get("usuario_nombre"))


@app.route("/carrito/agregar", methods=["POST"])
@login_requerido
def carrito_agregar():
    producto_id = request.form.get("producto_id", type=int)
    cantidad    = request.form.get("cantidad", type=int, default=1)
    if not producto_id:
        return redirect(url_for("productos"))
    carrito_id = get_or_create_carrito(session["usuario_id"])
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT id FROM carrito_items WHERE carrito_id = %s AND producto_id = %s",
                (carrito_id, producto_id))
    existente = cur.fetchone()
    if existente:
        cur.execute("UPDATE carrito_items SET cantidad = cantidad + %s WHERE id = %s",
                    (cantidad, existente["id"]))
    else:
        cur.execute("INSERT INTO carrito_items (carrito_id, producto_id, cantidad) VALUES (%s, %s, %s)",
                    (carrito_id, producto_id, cantidad))
    con.commit()
    con.close()
    return redirect(url_for("carrito"))


@app.route("/carrito/actualizar", methods=["POST"])
@login_requerido
def carrito_actualizar():
    item_id  = request.form.get("item_id", type=int)
    cantidad = request.form.get("cantidad", type=int)
    if not item_id:
        return redirect(url_for("carrito"))
    con = conectar()
    cur = con.cursor()
    if cantidad and cantidad > 0:
        cur.execute("UPDATE carrito_items SET cantidad = %s WHERE id = %s", (cantidad, item_id))
    else:
        cur.execute("DELETE FROM carrito_items WHERE id = %s", (item_id,))
    con.commit()
    con.close()
    return redirect(url_for("carrito"))


@app.route("/carrito/eliminar/<int:item_id>", methods=["POST"])
@login_requerido
def carrito_eliminar(item_id):
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM carrito_items WHERE id = %s", (item_id,))
    con.commit()
    con.close()
    return redirect(url_for("carrito"))


@app.route("/carrito/vaciar", methods=["POST"])
@login_requerido
def carrito_vaciar():
    carrito_id = get_or_create_carrito(session["usuario_id"])
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM carrito_items WHERE carrito_id = %s", (carrito_id,))
    con.commit()
    con.close()
    return redirect(url_for("carrito"))


# ══════════════════════════════════════════════════════
#  ADMIN
# ══════════════════════════════════════════════════════

@app.route("/admin")
@login_requerido
@admin_requerido
def admin():
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("""
        SELECT p.*, c.nombre AS categoria_nombre
        FROM productos p
        LEFT JOIN categorias c ON p.categoria_id = c.id
        ORDER BY p.fecha_creacion DESC
    """)
    productos = cur.fetchall()
    cur.execute("SELECT * FROM categorias ORDER BY nombre")
    categorias = cur.fetchall()
    cur.execute("SELECT COUNT(*) AS total FROM productos")
    total = cur.fetchone()["total"]
    cur.execute("SELECT COUNT(*) AS c FROM productos WHERE stock = 0")
    sin_stock = cur.fetchone()["c"]
    cur.execute("SELECT COUNT(*) AS c FROM productos WHERE stock > 0 AND stock <= 5")
    stock_bajo = cur.fetchone()["c"]
    con.close()
    return render_template("admin.html",
                           productos=productos,
                           categorias=categorias,
                           total=total,
                           sin_stock=sin_stock,
                           stock_bajo=stock_bajo,
                           usuario=session.get("usuario_nombre"))


@app.route("/admin/producto/nuevo", methods=["POST"])
@login_requerido
@admin_requerido
def admin_nuevo_producto():
    nombre       = request.form.get("nombre",       "").strip()
    descripcion  = request.form.get("descripcion",  "").strip()
    precio       = request.form.get("precio",       type=float)
    stock        = request.form.get("stock",        type=int, default=0)
    categoria_id = request.form.get("categoria_id", type=int)
    imagen       = request.form.get("imagen",       "").strip()
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        INSERT INTO productos (nombre, descripcion, precio, stock, categoria_id, imagen)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (nombre, descripcion, precio, stock, categoria_id, imagen or None))
    con.commit()
    con.close()
    return redirect(url_for("admin"))


@app.route("/admin/producto/editar/<int:id>", methods=["POST"])
@login_requerido
@admin_requerido
def admin_editar_producto(id):
    nombre       = request.form.get("nombre",       "").strip()
    descripcion  = request.form.get("descripcion",  "").strip()
    precio       = request.form.get("precio",       type=float)
    stock        = request.form.get("stock",        type=int, default=0)
    categoria_id = request.form.get("categoria_id", type=int)
    imagen       = request.form.get("imagen",       "").strip()
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        UPDATE productos
        SET nombre=%s, descripcion=%s, precio=%s, stock=%s, categoria_id=%s, imagen=%s
        WHERE id=%s
    """, (nombre, descripcion, precio, stock, categoria_id, imagen or None, id))
    con.commit()
    con.close()
    return redirect(url_for("admin"))


@app.route("/admin/producto/eliminar/<int:id>", methods=["POST"])
@login_requerido
@admin_requerido
def admin_eliminar_producto(id):
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM carrito_items WHERE producto_id = %s", (id,))
    cur.execute("DELETE FROM productos WHERE id = %s", (id,))
    con.commit()
    con.close()
    return redirect(url_for("admin"))


# ══════════════════════════════════════════════════════
#  API JSON
# ══════════════════════════════════════════════════════

@app.route("/api/categorias")
def api_categorias():
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM categorias ORDER BY nombre")
    cats = cur.fetchall()
    con.close()
    return jsonify(cats)


@app.route("/api/productos", methods=["GET", "POST"])
def api_productos():
    if request.method == "POST":
        if session.get("rol") != "admin":
            return jsonify({"error": "No autorizado"}), 403
        data         = request.get_json(force=True)
        nombre       = data.get("nombre",       "").strip()
        descripcion  = data.get("descripcion",  "").strip()
        precio       = data.get("precio")
        stock        = int(data.get("stock", 0))
        categoria_id = data.get("categoria_id")
        imagen       = data.get("imagen") or ""   # NOT NULL en BD → string vacío si no hay
        if not nombre or precio is None or not categoria_id:
            return jsonify({"error": "Faltan campos obligatorios"}), 400
        con = conectar()
        cur = con.cursor()
        cur.execute("""
            INSERT INTO productos (nombre, descripcion, precio, stock, categoria_id, imagen)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nombre, descripcion, float(precio), stock, categoria_id, imagen))
        con.commit()
        new_id = cur.lastrowid
        con.close()
        return jsonify({"ok": True, "id": new_id}), 201

    # GET
    cat_id     = request.args.get("categoria_id", type=int)
    buscar     = request.args.get("buscar",        default="").strip()
    orden      = request.args.get("orden",         default="nombre")
    pagina     = request.args.get("pagina",        type=int, default=1)
    por_pagina = request.args.get("por_pagina",    type=int, default=12)
    offset     = (pagina - 1) * por_pagina

    ordenes = {
        "nombre":      "p.nombre ASC",
        "precio_asc":  "p.precio ASC",
        "precio_desc": "p.precio DESC",
        "nuevo":       "p.fecha_creacion DESC",
    }
    order_sql = ordenes.get(orden, "p.nombre ASC")

    where  = ["1=1"]
    params = []
    if cat_id:
        where.append("p.categoria_id = %s")
        params.append(cat_id)
    if buscar:
        where.append("(p.nombre LIKE %s OR p.descripcion LIKE %s)")
        params += [f"%{buscar}%", f"%{buscar}%"]

    where_sql = " AND ".join(where)
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute(f"SELECT COUNT(*) AS total FROM productos p WHERE {where_sql}", params)
    total = cur.fetchone()["total"]
    cur.execute(f"""
        SELECT p.id, p.nombre, p.descripcion, p.precio, p.imagen,
               p.stock, p.categoria_id, c.nombre AS categoria_nombre
        FROM productos p
        LEFT JOIN categorias c ON p.categoria_id = c.id
        WHERE {where_sql}
        ORDER BY {order_sql}
        LIMIT %s OFFSET %s
    """, params + [por_pagina, offset])
    rows = cur.fetchall()
    con.close()
    for r in rows:
        r["precio"] = float(r["precio"])
    return jsonify({"productos": rows, "total": total, "pagina": pagina})


@app.route("/api/productos/<int:id>", methods=["GET", "PUT", "DELETE"])
def api_producto(id):
    if request.method == "PUT":
        if session.get("rol") != "admin":
            return jsonify({"error": "No autorizado"}), 403
        data         = request.get_json(force=True)
        nombre       = data.get("nombre",       "").strip()
        descripcion  = data.get("descripcion",  "").strip()
        precio       = data.get("precio")
        stock        = int(data.get("stock", 0))
        categoria_id = data.get("categoria_id")
        imagen       = data.get("imagen") or ""
        con = conectar()
        cur = con.cursor()
        cur.execute("""
            UPDATE productos
            SET nombre=%s, descripcion=%s, precio=%s, stock=%s, categoria_id=%s, imagen=%s
            WHERE id=%s
        """, (nombre, descripcion, float(precio), stock, categoria_id, imagen, id))
        con.commit()
        con.close()
        return jsonify({"ok": True})

    if request.method == "DELETE":
        if session.get("rol") != "admin":
            return jsonify({"error": "No autorizado"}), 403
        con = conectar()
        cur = con.cursor()
        cur.execute("DELETE FROM carrito_items WHERE producto_id = %s", (id,))
        cur.execute("DELETE FROM productos WHERE id = %s", (id,))
        con.commit()
        con.close()
        return jsonify({"ok": True})

    # GET
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("""
        SELECT p.*, c.nombre AS categoria_nombre
        FROM productos p
        LEFT JOIN categorias c ON p.categoria_id = c.id
        WHERE p.id = %s
    """, (id,))
    p = cur.fetchone()
    con.close()
    if not p:
        return jsonify({"error": "Producto no encontrado"}), 404
    p["precio"] = float(p["precio"])
    if p.get("fecha_creacion"):
        p["fecha_creacion"] = p["fecha_creacion"].isoformat()
    return jsonify(p)


@app.route("/api/carrito", methods=["GET", "POST"])
def api_carrito():
    if request.method == "POST":
        if "usuario_id" not in session:
            return jsonify({"error": "No autenticado"}), 401
        data        = request.get_json(force=True)
        producto_id = data.get("producto_id")
        cantidad    = int(data.get("cantidad", 1))
        carrito_id  = get_or_create_carrito(session["usuario_id"])
        con = conectar()
        cur = con.cursor(dictionary=True)
        cur.execute("SELECT id FROM carrito_items WHERE carrito_id=%s AND producto_id=%s",
                    (carrito_id, producto_id))
        existente = cur.fetchone()
        if existente:
            cur.execute("UPDATE carrito_items SET cantidad = cantidad + %s WHERE id = %s",
                        (cantidad, existente["id"]))
        else:
            cur.execute("INSERT INTO carrito_items (carrito_id, producto_id, cantidad) VALUES (%s,%s,%s)",
                        (carrito_id, producto_id, cantidad))
        con.commit()
        con.close()
        return jsonify({"ok": True})
    # GET
    if "usuario_id" not in session:
        return jsonify({"items": []}), 401
    carrito_id = get_or_create_carrito(session["usuario_id"])
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("""
        SELECT ci.id AS item_id, ci.cantidad,
               p.id AS producto_id, p.nombre, p.precio, p.imagen,
               c.nombre AS categoria_nombre
        FROM carrito_items ci
        JOIN productos p ON ci.producto_id = p.id
        LEFT JOIN categorias c ON p.categoria_id = c.id
        WHERE ci.carrito_id = %s
    """, (carrito_id,))
    items = cur.fetchall()
    con.close()
    for i in items:
        i["precio"] = float(i["precio"])
    return jsonify({"items": items})


@app.route("/api/carrito/<int:producto_id>", methods=["PUT", "DELETE"])
def api_carrito_item(producto_id):
    if "usuario_id" not in session:
        return jsonify({"error": "No autenticado"}), 401
    carrito_id = get_or_create_carrito(session["usuario_id"])
    con = conectar()
    cur = con.cursor()
    if request.method == "DELETE":
        cur.execute("DELETE FROM carrito_items WHERE carrito_id=%s AND producto_id=%s",
                    (carrito_id, producto_id))
    else:
        data     = request.get_json(force=True)
        cantidad = int(data.get("cantidad", 1))
        if cantidad > 0:
            cur.execute("UPDATE carrito_items SET cantidad=%s WHERE carrito_id=%s AND producto_id=%s",
                        (cantidad, carrito_id, producto_id))
        else:
            cur.execute("DELETE FROM carrito_items WHERE carrito_id=%s AND producto_id=%s",
                        (carrito_id, producto_id))
    con.commit()
    con.close()
    return jsonify({"ok": True})


# ══════════════════════════════════════════════════════
#  ARRANQUE
# ══════════════════════════════════════════════════════

if __name__ == "__main__":
    app.run(debug=True)