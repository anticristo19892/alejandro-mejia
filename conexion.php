<?php
$servidor = "localhost"; // o la IP de tu servidor MySQL
$usuario = "root"; // el nombre de usuario de MySQL
$clave = ""; // la contraseña de tu base de datos
$database = "jerezina"; // el nombre de la base de datos

// Crear la conexión
$conn = new mysqli($servidor, $usuario, $clave, $database);

// Verificar la conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}
echo "Conexión exitosa!". "<BR>";
?>

<?php
// Suponiendo que ya tienes la conexión abierta ($conn)
$sql = "SELECT * FROM estudiante";
$resultado = $conn->query($sql);

if ($resultado->num_rows > 0) {
    // Mostrar los datos de cada fila
    while($fila = $resultado->fetch_assoc()) {
        echo "id: " . $fila["id"]. " - Nombre: " . $fila["nombre"]. "<br>";
    }
} else {
    echo "0 resultados";
}

$conn->close(); // Cerrar la conexión
?>