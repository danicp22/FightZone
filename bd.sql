CREATE DATABASE FightZone;

USE FightZone;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    rol ENUM('cliente', 'admin') DEFAULT 'cliente',
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO usuarios (nombre, email, password, rol)
VALUES ('Administrador', 'admin@fightzone.com', 'Admin123!', 'admin')
ON DUPLICATE KEY UPDATE rol = 'admin';


CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    imagen VARCHAR(255) NOT NULL,
    categoria_id INT,
    stock INT DEFAULT 0,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

CREATE TABLE carrito (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE carrito_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    carrito_id INT,
    producto_id INT,
    cantidad INT DEFAULT 1,
    FOREIGN KEY (carrito_id) REFERENCES carrito(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);


INSERT INTO categorias (nombre) VALUES
('Guantes'),
('Sacos'),
('Proteccion'),
('Ropa'),
('Vendas');

CREATE USER "daniel"@"localhost" IDENTIFIED BY "Dani12345&";
GRANT ALL PRIVILEGES ON *.* TO "daniel"@"localhost";
FLUSH PRIVILEGES;

ALTER TABLE productos MODIFY imagen VARCHAR(1000) NOT NULL DEFAULT '';


-- Añadir para pedidos
 
CREATE TABLE IF NOT EXISTS pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    estado ENUM('pendiente','procesando','enviado','entregado','cancelado') DEFAULT 'pendiente',
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
 
CREATE TABLE IF NOT EXISTS pedido_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT NOT NULL,
    producto_id INT NOT NULL,
    nombre VARCHAR(150) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);
