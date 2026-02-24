<?php
?>
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FightZone</title>

  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>

<!-- Cursor -->
<div class="cur" id="cur"></div>
<div class="cur-r" id="curR"></div>

<!-- Toast -->
<div class="toast" id="toast">
  <div class="toast-icon">✓</div>
  <span>Añadido al carrito</span>
</div>

<!-- NAV -->
<nav>
  <a href="index.php" class="logo"><span class="logo-dot"></span> FightZone</a>

  <ul class="nav-links">
    <li><a href="#">Guantes</a></li>
    <li><a href="#">Sacos</a></li>
    <li><a href="#">Ropa</a></li>
    <li><a href="#">Protección</a></li>
    <li><a href="#">Vendas</a></li>
  </ul>

  <div class="nav-right">
    <a href="#" class="nav-cta">
      🛒 Carrito <span class="cart-badge" id="cCount">0</span>
    </a>

    <button class="hamburger" id="burger">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>

<div class="mobile-menu" id="mobileMenu">
  <a href="#">Guantes</a>
  <a href="#">Sacos</a>
  <a href="#">Ropa</a>
  <a href="#">Protección</a>
  <a href="#">Vendas</a>
</div>

<!-- HERO -->
<section class="hero">
  <div class="hero-left">
    <div class="hero-pill"><span class="hero-pill-dot"></span> Colección Élite 2025</div>

    <h1 class="hero-h1">
      El arte<br>de <span class="hi-red">luchar</span><br>
      <span class="hi-outline">sin límites</span>
    </h1>

    <p class="hero-desc">
      Equipamiento forjado para campeones.
    </p>

    <div class="hero-btns">
      <a href="#shop" class="btn-primary">Explorar tienda</a>
    </div>
  </div>
</section>

<!-- PRODUCTS -->
<section class="products-section" id="shop">
  <div class="sec-wrap">

    <div class="pgrid" id="pg">

      <div class="pcard" data-c="guantes">
        <div class="pinfo">
          <div class="pname">Guantes Pro Elite 16oz</div>
          <div class="pprice">89,95€</div>
          <button class="mobile-cart-btn">+ Añadir al carrito</button>
        </div>
      </div>

      <div class="pcard" data-c="proteccion">
        <div class="pinfo">
          <div class="pname">Casco Full Protection</div>
          <div class="pprice">59,95€</div>
          <button class="mobile-cart-btn">+ Añadir al carrito</button>
        </div>
      </div>

    </div>

  </div>
</section>

<footer>
  <div class="footer-inner">
    <div class="footer-copy">
      © 2025 FightZone — Todos los derechos reservados
    </div>
  </div>
</footer>

<script src="js/main.js"></script>
</body>
</html>