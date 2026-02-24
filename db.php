<?php
$host = "localhost";      
$user = "tu_usuario";     
$pass = "tu_contraseña";  
$dbname = "FightZone";   

$conn = new mysqli($host, $user, $pass, $dbname);

if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

$conn->set_charset("utf8");
?>