# app_query.py

from database_connector import DatabaseConnector

def get_muscles_list():
    # Création de l'objet DatabaseConnector et connexion à la base de données
    db_connector = DatabaseConnector()
    conn = db_connector.connect()

    # Création d'un curseur
    cursor = conn.cursor()
    
    # Requête SQL pour récupérer les muscles associés à un exercice
    query_el = """
    SELECT *
    FROM exercices
    """
    
    # Exécution des requêtes et récupération des résultats
    cursor.execute(query_el)
    exercice_list = cursor.fetchall()
    
    # Fermeture du curseur et de la connexion
    cursor.close()
    db_connector.close()
    
    # Retourner les résultats
    return exercice_list

def get_muscles_for_exercise(exercice_id):
    # Création de l'objet DatabaseConnector et connexion à la base de données
    db_connector = DatabaseConnector()
    conn = db_connector.connect()
    
    # Création d'un curseur
    cursor = conn.cursor()
    
    # Requête SQL pour récupérer les muscles associés à un exercice
    query_me = """
    SELECT m.id, m.nom
    FROM muscles m
    JOIN exercice_muscle em ON m.id = em.muscle_id
    WHERE em.exercice_id = %s
    """
    
    # Requête SQL pour récupérer le nom de l'exercice
    query_eid = """
    SELECT e.nom
    FROM exercices e
    WHERE e.id = %s
    """
    
    # Exécution des requêtes et récupération des résultats
    cursor.execute(query_me, (exercice_id,))
    muscles = cursor.fetchall()
    cursor.execute(query_eid, (exercice_id,))
    exercice_nom = cursor.fetchall()
    
    # Fermeture du curseur et de la connexion
    cursor.close()
    db_connector.close()
    
    # Retourner les résultats
    return exercice_nom, muscles
