-- Choix de la base si ce n'est pas déjà le cas
USE gym;

-- Insérer des utilisateurs
INSERT INTO utilisateurs (username, password, birthdate, sex, objectif) VALUES
('evanp', '0b14d501a594442a01c6859541bcb3e8164d183d32937b851835442f69d5c94e', '2000-02-11', 'M', true), -- password1
('romainhh', '6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4', '1999-07-25', 'M', false); -- password2

-- Exemples de muscles
INSERT INTO muscles (nom) VALUES
('Pectoraux'),
('Dorsaux'),
('Quadriceps'),
('Biceps'),
('Épaules'),
('Abdominaux'),
('Triceps'),
('Fessiers'),
('Ischio-jambiers'),
('Mollets'),
('Adducteurs'),
('Lombaires'),
('Trapèzes'),
('Deltoides');

5

-- Associer les exercices aux muscles
INSERT INTO exercice_muscle (exercice_id, muscle_id) VALUES
((SELECT id FROM exercices WHERE nom = 'Développé couché'), (SELECT id FROM muscles WHERE nom = 'Pectoraux')),
((SELECT id FROM exercices WHERE nom = 'Développé couché'), (SELECT id FROM muscles WHERE nom = 'Triceps')),
((SELECT id FROM exercices WHERE nom = 'Développé couché'), (SELECT id FROM muscles WHERE nom = 'Épaules')),
((SELECT id FROM exercices WHERE nom = 'Tirage vertical'), (SELECT id FROM muscles WHERE nom = 'Dorsaux')),
((SELECT id FROM exercices WHERE nom = 'Tirage vertical'), (SELECT id FROM muscles WHERE nom = 'Biceps')),
((SELECT id FROM exercices WHERE nom = 'Squat'), (SELECT id FROM muscles WHERE nom = 'Quadriceps')),
((SELECT id FROM exercices WHERE nom = 'Squat'), (SELECT id FROM muscles WHERE nom = 'Fessiers')),
((SELECT id FROM exercices WHERE nom = 'Curl biceps'), (SELECT id FROM muscles WHERE nom = 'Biceps')),
((SELECT id FROM exercices WHERE nom = 'Développé militaire'), (SELECT id FROM muscles WHERE nom = 'Épaules')),
((SELECT id FROM exercices WHERE nom = 'Développé militaire'), (SELECT id FROM muscles WHERE nom = 'Triceps')),
((SELECT id FROM exercices WHERE nom = 'Crunch'), (SELECT id FROM muscles WHERE nom = 'Abdominaux')),
((SELECT id FROM exercices WHERE nom = 'Soulevé de terre'), (SELECT id FROM muscles WHERE nom = 'Dorsaux')),
((SELECT id FROM exercices WHERE nom = 'Soulevé de terre'), (SELECT id FROM muscles WHERE nom = 'Quadriceps')),
((SELECT id FROM exercices WHERE nom = 'Extensions triceps'), (SELECT id FROM muscles WHERE nom = 'Triceps')),
((SELECT id FROM exercices WHERE nom = 'Fentes'), (SELECT id FROM muscles WHERE nom = 'Quadriceps')),
((SELECT id FROM exercices WHERE nom = 'Fentes'), (SELECT id FROM muscles WHERE nom = 'Fessiers')),
((SELECT id FROM exercices WHERE nom = 'Presse à cuisses'), (SELECT id FROM muscles WHERE nom = 'Quadriceps')),
((SELECT id FROM exercices WHERE nom = 'Presse à cuisses'), (SELECT id FROM muscles WHERE nom = 'Fessiers')),
((SELECT id FROM exercices WHERE nom = 'Élévation latérale'), (SELECT id FROM muscles WHERE nom = 'Deltoides')),
((SELECT id FROM exercices WHERE nom = 'Gainage'), (SELECT id FROM muscles WHERE nom = 'Abdominaux'));

-- Insertion d'exemples de données de santé
INSERT INTO health_data (username, weight, height, goal) VALUES
('evanp', 75.5, 185, true),
('romainhh', 67, 185, false);

-- Insertion d'exemples de statistiques personnelles
INSERT INTO personal_stats (username, neck, chest, waist, hips, thigh, calf, biceps, forearm, wrist, shoulders) VALUES
('evanp', 40, 100, 80, 95, 60, 40, 35, 28, 18, 110),
('romainhh', 38, 95, 75, 90, 55, 37, 32, 25, 16, 105);

--
-- Dumping data for table `planning`
--

LOCK TABLES `planning` WRITE;
/*!40000 ALTER TABLE `planning` DISABLE KEYS */;
INSERT INTO `planning` VALUES
(2,'romainhh','2024-06-15','10:00:00','11:30:00','x3 sessions de x10 rep - Dévellopé couché - 60Kg'),
(3,'romainhh','2024-06-15','15:00:00','17:00:00','x3 sessions de x20 rep - Pompes');
/*!40000 ALTER TABLE `planning` ENABLE KEYS */;
UNLOCK TABLES;