# app_cli.py

import os
import sys
from app import Applications
from app_planning import AppointmentManager
from app_query import get_muscles_for_exercise, get_exercices_list
from app_login import login, create_account, Utilisateur
from app_account_options import AccountOptions

class Terminal(Applications):
    project_name = "Python Terminal"
    project_version = float(1.0)

    """ Constructor """ 
    def __init__(self):    
        # Instance attributes
        self.terminal_state = "LOADING"
        self.user = None  # L'utilisateur n'est pas encore connecté

        self.initial_menu()

        self.appointment_manager = AppointmentManager()

        self.launch_app()
        self.app_main_menu()

    def initial_menu(self):
        while True:
            print("""
Bienvenue sur notre application !

Initial menu:
    1) Log in
    2) Create account
    3) Exit
            """)
            choice = input("Please enter your choice (1-3): ")

            if choice == '1':
                self.login_app()
                if self.user:
                    break
            elif choice == '2':
                create_account()
            elif choice == '3':
                self.quit_app()
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

    def login_app(self):
        user = login()
        if user:
            self.user = user  # Stockez l'instance utilisateur dans self.user
            #print(f"\nBienvenue, {self.user.username}!")
        else:
            print("Invalid credentials.")
            print("Exiting application.")
            self.quit_app()

    def launch_app(self):
        self.clear_terminal()
        print(f"Welcome to the {Terminal.project_name}")

    def app_main_menu (self):
        while True:
            print("""
Bienvenue""",self.user.username,"""

Main menu :
    1) Planning
    2) Options du compte
    3) Liste des exercices
    4) Muscles travaillés par un exercice
    5) Quitter Application
            """)

            choice = input("Please enter your choice (1-5): ")

            if choice == '1':
                self.planning_menu()
            elif choice == '2':
                self.account_options_app()
            elif choice == '3':
                self.ask_exercise_list()
            elif choice == '4':
                self.ask_exercise_id()
            elif choice == '5':
                self.quit_app()
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    def planning_menu(self):
        while True:
            print("""
Planning menu:
    1) Display calendar
    2) Display schedule for a date
    3) Add appointment
    4) Delete appointment
    5) Back to main menu
            """)
            choice = input("Please enter your choice (1-5): ")

            if choice == '1':
                #year = AppointmentManager.get_int_input("Enter year: ")
                #month = self.get_int_input("Enter month (1-12): ", 1, 12)
                #self.AppointmentManager.display_calendar(year, month)
                print(f"")
                year = int(input("Enter year: "))
                month = int(input("Enter month (1-12): "))
                self.appointment_manager.display_calendar(self.user.username, year, month)
            elif choice == '2':
                print(f"")
                date = input("Enter date (YYYY-MM-DD): ")
                self.appointment_manager.display_schedule(self.user.username, date)
            elif choice == '3':
                print(f"")
                date = input("Enter date for the appointment (YYYY-MM-DD): ")
                start_time = input("Enter start time for the appointment (HH:MM): ")
                end_time = input("Enter end time for the appointment (HH:MM): ")
                description = input("Enter description: ")
                self.appointment_manager.add_appointment(self.user.username, date, start_time, end_time, description)
            elif choice == '4':
                appointment_id = int(input("Enter the ID of the appointment to delete: "))
                self.appointment_manager.delete_appointment(appointment_id)
            elif choice == '5':
                break
            else:
                print(f"")
                print("Invalid choice. Please enter a number between 1 and 4.")

    def account_options_app(self):
        account_manager = AccountOptions(self.user.username)
        while True:
            print("""
Account Options:
    1) Delete Account
    2) Health Menu
    3) Personal Stats Menu
    4) Back to Main Menu
            """)
            choice = input("Please enter your choice (1-4): ")

            if choice == '1':
                account_manager.delete_account()
                print("Your account has been deleted. Exiting application.")
                self.quit_app()
            elif choice == '2':
                account_manager.health_menu()
            elif choice == '3':
                account_manager.personal_stats_menu()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    def ask_exercise_list(self):
        print(f"")
        exercice_list = get_exercices_list()
        for exercice in exercice_list :
            print(exercice[0], "-", exercice[1],
                  "\n\t--> Description :", exercice[2], 
                  "\n\t--> URL d'exemple :", exercice[3])
        print(f"")

    def ask_exercise_id(self):
        exercice_id = input("\nVeuillez renseigner le numéro d'ID de l'exercice pour afficher les muscles travaillés : ")
        
        # Utilisation de la fonction get_muscles_for_exercise depuis app_query.py
        exercice_nom, muscles = get_muscles_for_exercise(exercice_id)

        # Affichage des résultats
        if exercice_nom:
            print(f"Muscles associés à l'exercice ID {exercice_id} | {exercice_nom[0][0]} :")
            for muscle in muscles:
                print(f"ID: {muscle[0]}, Nom: {muscle[1]}")
        else:
            print(f"Aucun exercice trouvé avec l'ID {exercice_id}")

    def quit_app (self):
        exit()

    def clear_terminal(self):
        if(sys.platform == "win32"):
            os.system('cls')
        elif(sys.platform == "darwin"):
            os.system('clear')
        else:
            os.system('cls')