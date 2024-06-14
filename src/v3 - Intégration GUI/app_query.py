# app_query.py

from database_connector import DatabaseConnector

### Exercices

def get_exercices_list():
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

### Planning

def add_appointment(username, date, start_time, end_time, description):
    db_connector = DatabaseConnector()
    conn = db_connector.connect()
    cursor = conn.cursor()

    query = """
    INSERT INTO planning (username, date, start_time, end_time, description)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (username, date, start_time, end_time, description))
    conn.commit()

    cursor.close()
    db_connector.close()
    
    print(f"Appointment added on {date} from {start_time} to {end_time}: {description}")

def delete_appointment(appointment_id):
    db_connector = DatabaseConnector()
    conn = db_connector.connect()
    cursor = conn.cursor()

    query = "DELETE FROM planning WHERE id = %s"
    cursor.execute(query, (appointment_id,))
    conn.commit()

    cursor.close()
    db_connector.close()
    
    print(f"Appointment with ID {appointment_id} deleted.")

def get_schedule(username, date):
    db_connector = DatabaseConnector()
    conn = db_connector.connect()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM planning WHERE username = %s AND date = %s"
    cursor.execute(query, (username, date))
    appointments = cursor.fetchall()

    cursor.close()
    db_connector.close()
    
    return appointments

def get_appointment_dates(username, year, month):
    db_connector = DatabaseConnector()
    conn = db_connector.connect()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT DISTINCT date FROM planning 
    WHERE username = %s AND YEAR(date) = %s AND MONTH(date) = %s
    """
    cursor.execute(query, (username, year, month))
    appointment_dates = cursor.fetchall()

    cursor.close()
    db_connector.close()
    
    return appointment_dates

### Options du compte

def delete_account(username):
    db_connector = DatabaseConnector()
    conn = db_connector.connect()
    cursor = conn.cursor()
    
    query = "DELETE FROM utilisateurs WHERE username = %s"
    cursor.execute(query, (username,))
    conn.commit()
    
    cursor.close()
    db_connector.close()

def save_health_data(username, weight, height, goal):
    db_connector = DatabaseConnector()
    conn = db_connector.connect()
    cursor = conn.cursor()
    
    query = """
    INSERT INTO health_data (username, weight, height, goal, timestamp)
    VALUES (%s, %s, %s, %s, NOW())
    """
    cursor.execute(query, (username, weight, height, goal))
    conn.commit()
    
    cursor.close()
    db_connector.close()

def get_health_data(username):
    db_connector = DatabaseConnector()
    conn = db_connector.connect()
    cursor = conn.cursor()
    
    query = "SELECT * FROM health_data WHERE username = %s ORDER BY timestamp DESC"
    cursor.execute(query, (username,))
    health_data = cursor.fetchall()
    
    cursor.close()
    db_connector.close()
    
    return health_data

def save_personal_stats(username, **stats):
    db_connector = DatabaseConnector()
    conn = db_connector.connect()
    cursor = conn.cursor()
    
    columns = ', '.join(stats.keys())
    placeholders = ', '.join(['%s'] * len(stats))
    values = list(stats.values())
    
    query = f"""
    INSERT INTO personal_stats (username, {columns}, timestamp)
    VALUES (%s, {placeholders}, NOW())
    """
    cursor.execute(query, (username, *values))
    conn.commit()
    
    cursor.close()
    db_connector.close()

def get_personal_stats(username):
    db_connector = DatabaseConnector()
    conn = db_connector.connect()
    cursor = conn.cursor()
    
    query = "SELECT * FROM personal_stats WHERE username = %s ORDER BY timestamp DESC"
    cursor.execute(query, (username,))
    stats = cursor.fetchall()
    
    cursor.close()
    db_connector.close()
    
    return stats