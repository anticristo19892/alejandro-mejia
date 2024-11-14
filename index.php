<?php
// 3.php

// Accediendo al valor del campo 'nombre'
$nombre = $_GET['nombre'];
$edad = $_GET['edad'];
$email = $_GET['email'];
$interes = $_GET['interes'];
$sexo = $_GET['sexo'];
$area = $_GET['area'];

// Imprimiendo el valor recibido
echo "Hola, mi nombre es: " . $nombre ." <br>";
echo "Mi edad es:".$edad ." <br>";
echo "Mi Correo electronico es: ".$email ." <br>";
echo "Mi Curso de Interes es: " . $interes ." <br>";
echo "Mi Genero es: " .$sexo ." <br>";
echo "Mi Area de Interes es:  ".$area ." <br>";
?>
