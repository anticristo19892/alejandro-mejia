CREATE database emprendedores

CREATE TABLE ADMINISTRADOR(
id_administrador INT (08) PRIMARY KEY, 
nombre  VARCHAR (10),
apellido VARCHAR (11),
correo VARCHAR (20),
celular INT (13),
direccion VARCHAR (14)
);

CREATE TABLE mentores_experto(
id_mentor INT (21)PRIMARY KEY,
nombre VARCHAR (15),
apellido VARCHAR (16),
correo VARCHAR (17),
celular INT (18),
direccion VARCHAR (19)
);

CREATE TABLE emprendedores(
id_emprendedor INT (22) PRIMARY key,
nombre VARCHAR (23),
apellido VARCHAR (24),
correo VARCHAR (25),
celular INT (26),
direccion VARCHAR (27),
nombre_del_negocio VARCHAR (29)
);

DELIMITER $$

CREATE PROCEDURE Detalleemprendedores()
BEGIN
    SELECT * FROM emprendedores;
END$$

DELIMITER ;

CALL Detalleemprendedores();
DROP PROCEDURE Detalleemprendedores;



DELIMITER $$

CREATE PROCEDURE InsertarDatos(
    IN p_id_emprendedor INT,
    IN p_nombre VARCHAR(50),
    IN p_apellido VARCHAR(50),
    IN p_correo VARCHAR(100),
    IN p_celular VARCHAR(15),
    IN p_direccion VARCHAR(100),
    IN p_nombre_del_negocio VARCHAR(50)
)
BEGIN
    INSERT INTO emprendedores (id_emprendedor, nombre, apellido, correo, celular, direccion, nombre_del_negocio)
    VALUES (p_id_emprendedor, p_nombre, p_apellido, p_correo, p_celular, p_direccion, p_nombre_del_negocio);
END$$

DELIMITER ;


-- Ingreso de datos
CALL InsertarDatos('Doe', 'John', '1980-01-01 00:00:00', 'john_doe.jpg', 'Notes about John Doe');


DELIMITER $$

CREATE PROCEDURE Actualizaremprendedores(
    IN p_id_emprendedor INT,
    IN p_nombre VARCHAR(50),
    IN p_apellido VARCHAR(50),
    IN p_correo VARCHAR(100),
    IN p_celular VARCHAR(15),
    IN p_direccion VARCHAR(100),
    IN p_nombre_del_negocio VARCHAR(50)
)
BEGIN
    UPDATE emprendedores
    SET 
        nombre = p_nombre,
        apellido = p_apellido,
        correo = p_correo,
        celular = p_celular,
        direccion = p_direccion,
        nombre_del_negocio = p_nombre_del_negocio
    WHERE id_emprendedor = p_id_emprendedor;
END$$

DELIMITER ;

-- Actualizar datos
CALL Actualizaremprendedores(1, 'Doe', 'John', '1980-01-01 00:00:00', 'john_doe_updated.jpg', 'Updated notes about John Doe');


DELIMITER $$

CREATE PROCEDURE DeleteEmployee(
    IN p_emprendedoresID INTEGER
)
BEGIN
    DELETE FROM emprendedores
    WHERE emprendedoreID = p_emprendedoresID;
END$$

DELIMITER ;

-- Borrar datos
CALL Deleteemprendedores(12);

SELECT * FROM emprendedores 



DELIMITER $$

CREATE PROCEDURE GetemprendedoresByID(
    IN p_emprendedoresID INT
)
BEGIN
    SELECT 
        id_emprendedor,
        nombre,
        apellido,
        correo,
        celular,
        direccion,
        nombre_del_negocio
    FROM emprendedores
    WHERE id_emprendedor = p_emprendedoresID;
END$$

DELIMITER ;



CALL GetemprendedoresByID(1); 



