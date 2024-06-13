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

def create_account():
    db_connector = DatabaseConnector()
    conn = db_connector.connect()
    cursor = conn.cursor()
    
    while True:
        username = input("Choose a username: ")
        cursor.execute("SELECT * FROM utilisateurs WHERE username = %s", (username,))
        if cursor.fetchone():
            print("Username already taken. Please choose another one.")
        else:
            break

    while True:
        password = getpass("Choose a password: ")
        confirm_password = getpass("Confirm your password: ")
        if password != confirm_password:
            print("Passwords do not match. Please try again.")
        else:
            break

    cursor.execute("INSERT INTO utilisateurs (username, password, objectif) VALUES (%s, %s, %s)", (username, password, False))
    conn.commit()
    
    cursor.close()
    db_connector.close()
    
    print("Account created successfully. You can now log in.")
