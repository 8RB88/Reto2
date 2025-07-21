
-- Crear base de datos (si no existe)
CREATE DATABASE IF NOT EXISTS comparacion_carreras;
USE comparacion_carreras;

-- Crear tabla universidad
CREATE TABLE IF NOT EXISTS universidad (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE
);

-- Crear tabla carrera
CREATE TABLE IF NOT EXISTS carrera (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    universidad_id INT,
    FOREIGN KEY (universidad_id) REFERENCES universidad(id)
);

-- Crear tabla materia
CREATE TABLE IF NOT EXISTS materia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    nivel VARCHAR(10),
    carrera_id INT,
    FOREIGN KEY (carrera_id) REFERENCES carrera(id)
);

-- Crear tabla comparacion_materias
CREATE TABLE IF NOT EXISTS comparacion_materias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    materia_utpl_id INT,
    materia_unemi_id INT,
    score_similaridad DECIMAL(5,4),
    FOREIGN KEY (materia_utpl_id) REFERENCES materia(id),
    FOREIGN KEY (materia_unemi_id) REFERENCES materia(id)
);
