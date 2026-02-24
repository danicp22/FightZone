<?php
include "db.php";
include "header.php";

if(!isset($_SESSION['rol']) || $_SESSION['rol'] != 'admin') {
    die("Acceso denegado");
}

if($_SERVER['REQUEST_METHOD']=='POST'){
    $tabla = $_POST['categoria'];
    $nombre = $_POST['nombre'];
    $desc = $_POST['descripcion'];
    $precio = $_POST['precio'];
    $imagen = $_POST['imagen'];

    $stmt = $conn->prepare("INSERT INTO $tabla (nombre, descripcion, precio, imagen) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("ssis",$nombre,$desc,$precio,$imagen);

    if($stmt->execute()){
        echo "<p>Producto añadido correctamente</p>";
    } else {
        echo "<p>Error: ".$stmt->error."</p>";
    }
}
?>

<h2>Panel Administrador</h2>
<form method="POST" action="admin.php">
    <select name="categoria">
        <option value="guantes">Guantes</option>
        <option value="sacos">Sacos</option>
        <option value="ropa">Ropa</option>
        <option value="accesorios">Vendas</option>
    </select>
    <input type="text" name="nombre" placeholder="Nombre" required>
    <textarea name="descripcion" placeholder="Descripción"></textarea>
    <input type="number" step="0.01" name="precio" placeholder="Precio" required>
    <input type="text" name="imagen" placeholder="Ruta de imagen" required>
    <button type="submit">Añadir</button>
</form>

<?php include "footer.php"; ?>