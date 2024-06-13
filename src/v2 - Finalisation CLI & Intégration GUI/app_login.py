# app_login.py

from database_connector import DatabaseConnector
from getpass import getpass

class Utilisateur:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # Vous pouvez ajouter d'autres attributs ici en fonction de vos besoins

def login():
    db_connector = DatabaseConnector()
    conn = db_connector.connect()
    cursor = conn.cursor(dictionary=True)
    
    username = input("Username: ")
    password = getpass("Password: ")
    
    cursor.execute("SELECT * FROM utilisateurs WHERE username = %s AND password = %s", (username, password))
    user_data = cursor.fetchone()
    
    cursor.close()
    db_connector.close()
    
    if user_data:
        # Créez une instance de Utilisateur avec les données récupérées
        user = Utilisateur(username=user_data['username'], password=user_data['password'])
        # Vous pouvez ajouter d'autres attributs à partir de user_data si nécessaire
        return user
    else:
        return None

# Vous pouvez également ajouter d'autres fonctions ou méthodes liées à l'utilisateur ici si nécessaire
