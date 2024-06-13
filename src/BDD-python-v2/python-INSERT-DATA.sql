-- Choix de la base si ce n'est pas déjà le cas
USE gym;

-- Insérer des utilisateurs
INSERT INTO utilisateurs (username, password, objectif) VALUES
('evanp', 'password1', true),
('romainhh', 'password2', false);

-- Insérer des muscles
INSERT INTO muscles (nom) VALUES
('Pectoraux'),
('Dorsaux'),
('Quadriceps'),
('Biceps'),
('Épaules'),
('Abdominaux'),
('Triceps'),
('Fessiers');

-- Insérer des exercices
INSERT INTO exercices (nom, description, video_url) VALUES
('Développé couché', 'Exercice de musculation ciblant principalement les pectoraux.', 'http://example.com/video/developpe_couche'),
('Tirage vertical', 'Exercice pour le dos ciblant les dorsaux.', 'http://example.com/video/tirage_vertical'),
('Squat', 'Exercice de musculation pour les jambes.', 'http://example.com/video/squat'),
('Curl biceps', 'Exercice d\'isolement pour les biceps.', 'http://example.com/video/curl_biceps'),
('Développé militaire', 'Exercice de musculation pour les épaules.', 'http://example.com/video/developpe_militaire'),
('Crunch', 'Exercice pour les abdominaux.', 'http://example.com/video/crunch');

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
((SELECT id FROM exercices WHERE nom = 'Crunch'), (SELECT id FROM muscles WHERE nom = 'Abdominaux'));
