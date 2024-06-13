-- Création de la base de données
CREATE DATABASE gym;
USE gym;

CREATE USER 'admin'@'%' IDENTIFIED BY 'MotDePasse999!';
GRANT ALL PRIVILEGES ON gym.* TO 'admin'@'%';
FLUSH PRIVILEGES;

-- Table UTILISATEUR
CREATE TABLE utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    objectif BOOLEAN NOT NULL -- true pour 'prise de masse', false pour 'perte de poids'
);

-- Table PARTIE_DU_CORPS
CREATE TABLE muscles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL
);

-- Table EXERCICE
CREATE TABLE exercices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    description TEXT,
    video_url VARCHAR(255)
);

-- Table de jointure EXERCICE_MUSCLE
CREATE TABLE exercice_muscle (
    exercice_id INT NOT NULL,
    muscle_id INT NOT NULL,
    PRIMARY KEY (exercice_id, muscle_id),
    FOREIGN KEY (exercice_id) REFERENCES exercices(id) ON DELETE CASCADE,
    FOREIGN KEY (muscle_id) REFERENCES muscles(id) ON DELETE CASCADE
);

-- Table PLANNING
CREATE TABLE planning (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    description TEXT,
    FOREIGN KEY (username) REFERENCES utilisateurs(username) ON DELETE CASCADE
);
