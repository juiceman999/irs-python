"""

@author : Romain Hénon-Hilaire

"""

import os
import sys
from app import Applications
from app_planning import AppointmentManager
from app_query import get_muscles_for_exercise, get_exercices_list
from app_login import login, create_account, Utilisateur
from app_account_options import AccountOptions

class Terminal(Applications):
    project_name = "Terminal Python"
    project_version = float(1.0)

    """ Constructeur """ 
    def __init__(self):    
        # Attributs d'instance
        self.terminal_state = "CHARGEMENT"
        self.user = None  # L'utilisateur n'est pas encore connecté

        self.initial_menu()

        self.appointment_manager = AppointmentManager()

        self.launch_app()
        self.app_main_menu()

    def initial_menu(self):
        while True:
            print("""
Bienvenue sur notre application !

Menu initial :
    1) Se connecter
    2) Créer un compte
    3) Quitter
            """)
            choice = input("Veuillez entrer votre choix (1-3) : ")

            if choice == '1':
                self.login_app()
                if self.user:
                    break
            elif choice == '2':
                create_account()
            elif choice == '3':
                self.quit_app()
            else:
                print("Choix invalide. Veuillez entrer un numéro entre 1 et 3.")

    def login_app(self):
        user = login()
        if user:
            self.user = user  # Stocke l'instance utilisateur dans self.user
            #print(f"\nBienvenue, {self.user.username}!")
        else:
            print("Identifiants invalides.")
            print("Fermeture de l'application.")
            self.quit_app()

    def launch_app(self):
        self.clear_terminal()
        print(f"Bienvenue dans {Terminal.project_name}")

    def app_main_menu(self):
        while True:
            print(f"""
Bienvenue, {self.user.username} !

Menu principal :
    1) Planning
    2) Menu Exercices
    3) Options du compte
    4) Quitter l'application
            """)

            choice = input("Veuillez entrer votre choix (1-4) : ")

            if choice == '1':
                self.planning_menu()
            elif choice == '2':
                self.exercises_menu()
            elif choice == '3':
                self.account_options_app()
            elif choice == '4':
                self.quit_app()
            else:
                print("Choix invalide. Veuillez entrer un numéro entre 1 et 4.")

    def planning_menu(self):
        while True:
            print("""
Menu Planning :
    1) Afficher le calendrier
    2) Afficher l'horaire pour une date
    3) Ajouter un rendez-vous
    4) Supprimer un rendez-vous
    5) Retour au menu principal
            """)
            choice = input("Veuillez entrer votre choix (1-5) : ")

            if choice == '1':
                year = int(input("Entrez l'année : "))
                month = int(input("Entrez le mois (1-12) : "))
                self.appointment_manager.display_calendar(self.user.username, year, month)
            elif choice == '2':
                date = input("Entrez la date (YYYY-MM-DD) : ")
                self.appointment_manager.display_schedule(self.user.username, date)
            elif choice == '3':
                date = input("Entrez la date du rendez-vous (YYYY-MM-DD) : ")
                start_time = input("Entrez l'heure de début du rendez-vous (HH:MM) : ")
                end_time = input("Entrez l'heure de fin du rendez-vous (HH:MM) : ")
                description = input("Entrez la description : ")
                self.appointment_manager.add_appointment(self.user.username, date, start_time, end_time, description)
            elif choice == '4':
                appointment_id = int(input("Entrez l'ID du rendez-vous à supprimer : "))
                self.appointment_manager.delete_appointment(appointment_id)
            elif choice == '5':
                break
            else:
                print("Choix invalide. Veuillez entrer un numéro entre 1 et 5.")

    def account_options_app(self):
        account_manager = AccountOptions(self.user.username)
        while True:
            print("""
Options du compte :
    1) Supprimer le compte
    2) Menu Santé
    3) Menu Statistiques Personnelles
    4) Retour au menu principal
            """)
            choice = input("Veuillez entrer votre choix (1-4) : ")

            if choice == '1':
                account_manager.delete_account()
                print("Votre compte a été supprimé. Fermeture de l'application.")
                self.quit_app()
            elif choice == '2':
                account_manager.health_menu()
            elif choice == '3':
                account_manager.personal_stats_menu()
            elif choice == '4':
                break
            else:
                print("Choix invalide. Veuillez entrer un numéro entre 1 et 4.")

    def exercises_menu(self):
        while True:
            print("""
Menu Exercices :
    1) Liste des Exercices
    2) Muscles travaillés par un Exercice
    3) Retour au menu principal
            """)
            choice = input("Veuillez entrer votre choix (1-3) : ")

            if choice == '1':
                self.ask_exercise_list()
            elif choice == '2':
                self.ask_exercise_id()
            elif choice == '3':
                break
            else:
                print("Choix invalide. Veuillez entrer un numéro entre 1 et 3.")

    def ask_exercise_list(self):
        print(f"")
        exercice_list = get_exercices_list()
        for exercice in exercice_list:
            print(exercice[0], "-", exercice[1],
                  "\n\t--> Description :", exercice[2],
                  "\n\t--> URL de la vidéo :", exercice[3])

    def ask_exercise_id(self):
        exercice_id = input("\nEntrez l'ID de l'exercice pour afficher les muscles travaillés : ")
        
        # Utilisation de la fonction get_muscles_for_exercise depuis app_query.py
        exercice_nom, muscles = get_muscles_for_exercise(exercice_id)

        # Affichage des résultats
        if exercice_nom:
            print(f"Muscles travaillés par l'exercice ID {exercice_id} | {exercice_nom[0][0]} :")
            for muscle in muscles:
                print(f"ID : {muscle[0]}, Nom : {muscle[1]}")
        else:
            print(f"Aucun exercice trouvé avec l'ID {exercice_id}")

    def quit_app(self):
        exit()

    def clear_terminal(self):
        if(sys.platform == "win32"):
            os.system('cls')
        elif(sys.platform == "darwin"):
            os.system('clear')
        else:
            os.system('cls')

