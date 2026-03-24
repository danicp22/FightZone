// ══════════════════════════════════════════════════════
//  FightZone — Sistema de traducción ES / EN
//  Uso: incluir este script en todos los templates
//  El idioma se guarda en localStorage ('fz_lang')
// ══════════════════════════════════════════════════════

const TRANSLATIONS = {

  // ── GLOBAL (nav, footer, elementos comunes) ────────
  "nav.inicio":        { es: "Inicio",        en: "Home" },
  "nav.productos":     { es: "Productos",     en: "Products" },
  "nav.quienes":       { es: "Quienes Somos", en: "About Us" },
  "nav.cuenta":        { es: "Mi cuenta",     en: "My account" },
  "nav.carrito":       { es: "Carrito",       en: "Cart" },
  "nav.admin":         { es: "Panel admin",   en: "Admin panel" },
  "nav.logout":        { es: "Cerrar sesión", en: "Log out" },

  "footer.tagline":    { es: "Equipamiento premium para atletas que no se conforman con menos.", en: "Premium equipment for athletes who settle for nothing less." },
  "footer.tienda":     { es: "Shop",          en: "Shop" },
  "footer.ayuda":      { es: "Help",          en: "Help" },
  "footer.legal":      { es: "Legal",         en: "Legal" },
  "footer.envios":     { es: "Envíos",        en: "Shipping" },
  "footer.devoluciones":{ es: "Devoluciones", en: "Returns" },
  "footer.tallas":     { es: "Tallas",        en: "Sizes" },
  "footer.contacto":   { es: "Contacto",      en: "Contact" },
  "footer.privacidad": { es: "Privacidad",    en: "Privacy" },
  "footer.terminos":   { es: "Términos",      en: "Terms" },
  "footer.cookies":    { es: "Cookies",       en: "Cookies" },
  "footer.copy":       { es: "© 2026 FightZone — Todos los derechos reservados", en: "© 2026 FightZone — All rights reserved" },

  // ── INDEX ──────────────────────────────────────────
  "index.pill":        { es: "Colección Élite 2026",   en: "Elite Collection 2026" },
  "index.h1a":         { es: "El arte",                en: "The art" },
  "index.h1b":         { es: "luchar",                 en: "of fighting" },
  "index.h1c":         { es: "sin límites",            en: "without limits" },
  "index.desc":        { es: "Equipamiento forjado para campeones. Diseñado con precisión para rendir cuando más importa.", en: "Equipment forged for champions. Designed with precision to perform when it matters most." },
  "index.explorar":    { es: "🔥 Explorar tienda",     en: "🔥 Explore store" },
  "index.productos":   { es: "Productos",              en: "Products" },
  "index.marcas":      { es: "Marcas",                 en: "Brands" },
  "index.envio":       { es: "Envío rápido",           en: "Fast shipping" },
  "index.envio_sub":   { es: "24-48h España",          en: "24-48h Spain" },
  "index.devuelves":   { es: "Devuelves gratis",       en: "Free returns" },
  "index.devuelves_sub":{ es: "30 días",               en: "30 days" },

  "cats.eyebrow":      { es: "Explorar",               en: "Explore" },
  "cats.title":        { es: "Todas las",              en: "All" },
  "cats.title_i":      { es: "categorías",             en: "categories" },
  "cats.vertodo":      { es: "Ver todo →",             en: "View all →" },
  "cats.guantes":      { es: "Guantes",                en: "Gloves" },
  "cats.ropa":         { es: "Ropa",                   en: "Clothing" },
  "cats.proteccion":   { es: "Protección",             en: "Protection" },
  "cats.sacos":        { es: "Sacos",                  en: "Bags" },
  "cats.vendas":       { es: "Vendas",                 en: "Wraps" },
  "cats.productos":    { es: "productos",              en: "products" },

  "feat.eyebrow":      { es: "Producto del Mes",       en: "Product of the Month" },
  "feat.desc":         { es: "Cuero genuino de primera calidad con relleno de élite. Diseñado para los entrenamientos más exigentes, durante años.", en: "Genuine premium leather with elite padding. Designed for the most demanding training sessions, for years." },
  "feat.add":          { es: "🛒 Añadir al carrito",   en: "🛒 Add to cart" },
  "feat.peso":         { es: "Peso",                   en: "Weight" },
  "feat.cuero":        { es: "Cuero",                  en: "Leather" },
  "feat.garantia":     { es: "Garantía",               en: "Warranty" },
  "feat.anios":        { es: "5 años",                 en: "5 years" },

  "testi.eyebrow":     { es: "Reseñas",                en: "Reviews" },
  "testi.title":       { es: "Lo que",                 en: "What they" },
  "testi.title_i":     { es: "dicen",                  en: "say" },
  "testi.vertodas":    { es: "Ver todas →",            en: "View all →" },
  "testi.role1":       { es: "Boxeador Profesional",   en: "Professional Boxer" },
  "testi.role2":       { es: "Entrenadora Muay Thai",  en: "Muay Thai Coach" },
  "testi.role3":       { es: "Campeón Regional 2024",  en: "Regional Champion 2024" },
  "testi.t1":          { es: "Los mejores guantes que he probado en mis 10 años entrenando. La calidad es brutal y aguantan sesiones muy intensas sin deformarse.", en: "The best gloves I've tried in my 10 years of training. The quality is outstanding and they hold up through the most intense sessions." },
  "testi.t2":          { es: "Vaya ruina de pagina, me han estafado, el envio tardo 3 semanas y la caja estaba rota.", en: "What a terrible website, I was scammed, delivery took 3 weeks and the box was broken." },
  "testi.t3":          { es: "Increíble variedad y atención al cliente de 10. Llegó en 24h perfectamente embalado. Mi tienda de referencia para todo el equipo.", en: "Incredible variety and top-notch customer service. Arrived in 24h perfectly packed. My go-to store for all the team." },

  "nl.eyebrow":        { es: "Newsletter",             en: "Newsletter" },
  "nl.title":          { es: "Entrena con",            en: "Train with" },
  "nl.title_i":        { es: "ventaja",                en: "an edge" },
  "nl.sub":            { es: "Ofertas exclusivas, lanzamientos anticipados y consejos de los mejores entrenadores directo a tu bandeja.", en: "Exclusive deals, early launches and tips from top coaches straight to your inbox." },
  "nl.placeholder":    { es: "tu@email.com",           en: "you@email.com" },
  "nl.btn":            { es: "Unirme →",               en: "Join →" },

  "ticker.1":          { es: "Guantes de calidad",     en: "Quality gloves" },
  "ticker.2":          { es: "Envío Gratis +50€",      en: "Free Shipping +50€" },
  "ticker.3":          { es: "Ofertas - hasta 30%",    en: "Deals - up to 30% off" },
  "ticker.4":          { es: "Nuevos Sacos exclusivos",en: "New exclusive bags" },
  "ticker.5":          { es: "Devolución 30 Días",     en: "30-Day Returns" },

  // ── PRODUCTOS ─────────────────────────────────────
  "productos.title":   { es: "Todos los",              en: "All" },
  "productos.title_i": { es: "productos",              en: "products" },
  "productos.cargando":{ es: "Cargando productos…",    en: "Loading products…" },
  "productos.buscar":  { es: "Buscar productos…",      en: "Search products…" },
  "productos.btn_buscar":{ es: "Buscar",               en: "Search" },
  "productos.todos":   { es: "Todos",                  en: "All" },
  "productos.orden_nombre":{ es: "Nombre A-Z",         en: "Name A-Z" },
  "productos.orden_precio_asc":{ es: "Precio: menor a mayor", en: "Price: low to high" },
  "productos.orden_precio_desc":{ es: "Precio: mayor a menor", en: "Price: high to low" },
  "productos.orden_nuevo":{ es: "Más nuevos",          en: "Newest" },
  "productos.anadir":  { es: "+ Añadir",               en: "+ Add" },
  "productos.anadir_carrito":{ es: "+ Añadir al carrito", en: "+ Add to cart" },
  "productos.sin_stock":{ es: "Sin stock",             en: "Out of stock" },
  "productos.en_stock":{ es: "✓ En stock",             en: "✓ In stock" },
  "productos.ultimas": { es: "⚠ Últimas",              en: "⚠ Last" },
  "productos.vacío_t": { es: "Sin resultados",         en: "No results" },
  "productos.vacío_d": { es: "No hay productos con estos filtros.\nPrueba con otra búsqueda o categoría.", en: "No products match these filters.\nTry a different search or category." },
  "productos.ver_todos":{ es: "Ver todos los productos →", en: "View all products →" },
  "productos.anterior":{ es: "← Anterior",            en: "← Previous" },
  "productos.siguiente":{ es: "Siguiente →",           en: "Next →" },
  "productos.toast":   { es: "Añadido al carrito",     en: "Added to cart" },

  // ── PRODUCTO INDIVIDUAL ────────────────────────────
  "producto.volver":   { es: "← Volver al catálogo",  en: "← Back to catalog" },
  "producto.inicio":   { es: "Inicio",                 en: "Home" },
  "producto.cargando": { es: "Cargando…",              en: "Loading…" },
  "producto.sin_stock":{ es: "Sin stock",              en: "Out of stock" },
  "producto.en_stock": { es: "✓ En stock",             en: "✓ In stock" },
  "producto.ultimas":  { es: "⚠ Últimas",              en: "⚠ Last" },
  "producto.unidades": { es: "unidades",               en: "units" },
  "producto.cantidad": { es: "Cantidad",               en: "Quantity" },
  "producto.anadir":   { es: "🛒 Añadir al carrito",   en: "🛒 Add to cart" },
  "producto.toast":    { es: "añadido al carrito",     en: "added to cart" },
  "producto.envio_t":  { es: "Envío gratuito",         en: "Free shipping" },
  "producto.envio_d":  { es: "+50€ envío gratis",      en: "+50€ free shipping" },
  "producto.dev_t":    { es: "Devolución fácil",       en: "Easy returns" },
  "producto.dev_d":    { es: "30 días sin preguntas",  en: "30 days no questions" },
  "producto.pago_t":   { es: "Pago seguro",            en: "Secure payment" },
  "producto.pago_d":   { es: "Encriptado SSL",         en: "SSL encrypted" },
  "producto.stock_t":  { es: "Stock",                  en: "Stock" },
  "producto.no_encontrado":{ es: "Producto no encontrado", en: "Product not found" },

  // ── CARRITO ────────────────────────────────────────
  "carrito.title":     { es: "Tu",                     en: "Your" },
  "carrito.title_i":   { es: "carrito",                en: "cart" },
  "carrito.vacio_t":   { es: "Tu carrito está vacío",  en: "Your cart is empty" },
  "carrito.vacio_d":   { es: "Añade productos para empezar a comprar.", en: "Add products to start shopping." },
  "carrito.ver_productos":{ es: "Ver productos →",     en: "View products →" },
  "carrito.vaciar":    { es: "Vaciar carrito",         en: "Clear cart" },
  "carrito.resumen":   { es: "Resumen del pedido",     en: "Order summary" },
  "carrito.subtotal":  { es: "Subtotal",               en: "Subtotal" },
  "carrito.envio":     { es: "Envío",                  en: "Shipping" },
  "carrito.gratis":    { es: "Gratis",                 en: "Free" },
  "carrito.descuento": { es: "Descuento",              en: "Discount" },
  "carrito.total":     { es: "Total",                  en: "Total" },
  "carrito.pagar":     { es: "Finalizar compra →",     en: "Checkout →" },
  "carrito.cupon":     { es: "Código de descuento",    en: "Discount code" },
  "carrito.cupon_ph":  { es: "FIGHT10",                en: "FIGHT10" },
  "carrito.aplicar":   { es: "Aplicar",                en: "Apply" },
  "carrito.envio_std": { es: "Estándar (gratis +50€)", en: "Standard (free +50€)" },
  "carrito.envio_exp": { es: "Express 24h (4,95€)",    en: "Express 24h (€4.95)" },
  "carrito.cargando":  { es: "Cargando tu carrito…",   en: "Loading your cart…" },

  // ── LOGIN ──────────────────────────────────────────
  "login.title":       { es: "Iniciar",                en: "Log" },
  "login.title_i":     { es: "sesión",                 en: "in" },
  "login.sub":         { es: "Accede con tu cuenta de FightZone", en: "Sign in to your FightZone account" },
  "login.email":       { es: "Correo electrónico",     en: "Email address" },
  "login.password":    { es: "Contraseña",             en: "Password" },
  "login.btn":         { es: "Entrar",                 en: "Sign in" },
  "login.no_cuenta":   { es: "¿No tienes cuenta?",     en: "Don't have an account?" },
  "login.registro":    { es: "Regístrate gratis",       en: "Sign up for free" },

  // ── REGISTRO ──────────────────────────────────────
  "registro.title":    { es: "Crear",                  en: "Create" },
  "registro.title_i":  { es: "cuenta",                 en: "account" },
  "registro.sub":      { es: "Es gratis, siempre lo será", en: "It's free, always will be" },
  "registro.nombre":   { es: "Nombre",                 en: "First name" },
  "registro.apellido": { es: "Apellidos",              en: "Last name" },
  "registro.email":    { es: "Correo electrónico",     en: "Email address" },
  "registro.password": { es: "Contraseña",             en: "Password" },
  "registro.rep_pass": { es: "Repite la contraseña",   en: "Confirm password" },
  "registro.continuar":{ es: "Continuar →",            en: "Continue →" },
  "registro.ya_cuenta":{ es: "¿Ya tienes cuenta?",     en: "Already have an account?" },
  "registro.iniciar":  { es: "Inicia sesión",          en: "Sign in" },
  "registro.crear":    { es: "Crear mi cuenta",        en: "Create my account" },
  "registro.terminos": { es: "Acepto los términos y condiciones", en: "I accept the terms and conditions" },
  "registro.bienvenido":{ es: "¡Bienvenido a", en: "Welcome to" },

  // ── INFO / QUIÉNES SOMOS ──────────────────────────
  "info.hero_eyebrow": { es: "Quiénes somos",          en: "About us" },
  "info.jobs_eyebrow": { es: "Únete al equipo",        en: "Join the team" },
  "info.jobs_title":   { es: "Trabaja con",            en: "Work with" },
  "info.jobs_title_i": { es: "nosotros",               en: "us" },
  "info.jobs_desc":    { es: "En FightZone buscamos personas apasionadas por el deporte de combate. Si quieres formar parte de un equipo joven y en crecimiento, envíanos tu candidatura.", en: "At FightZone we look for people passionate about combat sports. If you want to be part of a young and growing team, send us your application." },
  "info.jobs_btn":     { es: "Enviar candidatura →",   en: "Send application →" },
  "info.maps_btn":     { es: "📌 Abrir en Google Maps", en: "📌 Open in Google Maps" },
};

// ── Motor de traducción ────────────────────────────────
(function() {
  const LANG_KEY = 'fz_lang';

  function getLang() {
    return localStorage.getItem(LANG_KEY) || 'es';
  }

  function setLang(lang) {
    localStorage.setItem(LANG_KEY, lang);
    applyLang(lang);
    updateBtn(lang);
  }

  function t(key) {
    const entry = TRANSLATIONS[key];
    if (!entry) return key;
    return entry[getLang()] || entry['es'] || key;
  }

  function applyLang(lang) {
    // Traducir todos los elementos con data-i18n
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      const entry = TRANSLATIONS[key];
      if (!entry) return;
      const val = entry[lang] || entry['es'];
      // Si es input/textarea, traducir placeholder
      if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
        el.placeholder = val;
      } else {
        el.textContent = val;
      }
    });
    // Actualizar lang del html
    document.documentElement.lang = lang;
  }

  function updateBtn(lang) {
    const btn = document.getElementById('langToggleBtn');
    if (!btn) return;
    if (lang === 'es') {
      btn.innerHTML = '<span class="lang-flag">🇬🇧</span><span class="lang-label">EN</span>';
      btn.title = 'Switch to English';
    } else {
      btn.innerHTML = '<span class="lang-flag">🇪🇸</span><span class="lang-label">ES</span>';
      btn.title = 'Cambiar a Español';
    }
  }

  // Exponer globalmente
  window.FZLang = { t, getLang, setLang, applyLang };

  // Auto-aplicar al cargar el DOM
  document.addEventListener('DOMContentLoaded', function() {
    const lang = getLang();
    applyLang(lang);
    updateBtn(lang);

    const btn = document.getElementById('langToggleBtn');
    if (btn) {
      btn.addEventListener('click', () => {
        setLang(getLang() === 'es' ? 'en' : 'es');
      });
    }
  });
})();
