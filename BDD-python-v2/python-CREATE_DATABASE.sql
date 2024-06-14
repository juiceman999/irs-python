-- Création de la base de données gym (si elle n'existe pas déjà)
CREATE DATABASE IF NOT EXISTS gym;
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

-- Table health_data pour stocker les données de santé des utilisateurs
CREATE TABLE IF NOT EXISTS health_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    weight FLOAT NOT NULL, -- Poids en kg
    height FLOAT NOT NULL, -- Taille en cm
    birthdate DATE NOT NULL,
    sex ENUM('M', 'F') NOT NULL,
    goal BOOLEAN NOT NULL, -- true pour 'prise de masse', false pour 'perte de poids'
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (username) REFERENCES utilisateurs(username) ON DELETE CASCADE
);

-- Table personal_stats pour stocker les statistiques personnelles des utilisateurs
CREATE TABLE IF NOT EXISTS personal_stats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    neck FLOAT, -- Tour de cou en cm
    chest FLOAT, -- Tour de poitrine en cm
    waist FLOAT, -- Tour de taille en cm
    hips FLOAT, -- Tour de hanches en cm
    thigh FLOAT, -- Tour de cuisse en cm
    calf FLOAT, -- Tour de mollet en cm
    biceps FLOAT, -- Tour de biceps en cm
    forearm FLOAT, -- Tour d'avant-bras en cm
    wrist FLOAT, -- Tour de poignet en cm
    shoulders FLOAT, -- Tour d'épaules en cm
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (username) REFERENCES utilisateurs(username) ON DELETE CASCADE
);