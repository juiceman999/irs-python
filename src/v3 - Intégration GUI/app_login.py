# app_login.py

from database_connector import DatabaseConnector
from getpass import getpass
import hashlib
import datetime

class Utilisateur:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # Vous pouvez ajouter d'autres attributs ici en fonction de vos besoins

def login():
    db_connector = DatabaseConnector()
    conn = db_connector.connect()
    cursor = conn.cursor(dictionary=True)
    

    # Si en CLI
    username = input("Username: ")
    password = getpass("Password: ")

    # Si en GUI
    ###

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    cursor.execute("SELECT * FROM utilisateurs WHERE username = %s AND password = %s", (username, hashed_password))
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

def login_with_gui(username, password):
    db_connector = DatabaseConnector()
    conn = db_connector.connect()
    cursor = conn.cursor(dictionary=True)

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    cursor.execute("SELECT * FROM utilisateurs WHERE username = %s AND password = %s", (username, hashed_password))
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
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            break
    
    while True:
        birthdate = input("Entrez votre date de naissance (format YYYY-MM-DD) : ")
        try:
            birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Format de date incorrect. Assurez-vous d'utiliser le format YYYY-MM-DD.")

    while True:
        sex = input("Entrez votre sexe (M/F) : ").upper()
        if sex == 'M' or sex == 'F':
            break
        else:
            print("Sexe incorrect. Veuillez entrer 'M' pour masculin ou 'F' pour féminin.")

    cursor.execute("INSERT INTO utilisateurs (username, password, birthdate, sex, objectif) VALUES (%s, %s, %s, %s, %s)", (username, hashed_password, birthdate, sex, False))
    conn.commit()
    
    cursor.close()
    db_connector.close()
    
    print("Account created successfully. You can now log in.")
