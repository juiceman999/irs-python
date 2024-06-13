import os
import sys
from app import Applications
from app_planning import AppointmentManager
from app_query import get_muscles_for_exercise, get_muscles_list

class Terminal(Applications):
    project_name = "Python Terminal"
    project_version = float(1.0)

    """ Constructor """ 
    def __init__(self):    
        # Instance attributes
        self.terminal_state = "LOADING"
        
        self.launch_app()
        self.app_main_menu()

    def launch_app(self):
        self.clear_terminal()
        print(f"Welcome to the {Terminal.project_name}")

    def app_main_menu (self):
        while True:
            print("""
Main menu :
    1) Planning
    2) Options
    3) Liste des exercices
    4) Muscles travaillés par un exercice
    5) Quitter Application
            """)
        
            choice = input("Please enter your choice (1-5): ")

            if choice == '1':
                self.planning_menu()
            elif choice == '2':
                self.option_app()
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
            print("\nPlanning menu:\n  1) Display schedule for a date\n  2) Add appointment\n  3) Display calendar\n  4) Back to main menu")
            choice = input("Please enter your choice (1-4): ")

            if choice == '1':
                date = input("Enter date (YYYY-MM-DD): ")
                self.AppointmentManager.display_schedule(date)
            elif choice == '2':
                date = input("Enter date for the appointment (YYYY-MM-DD): ")
                start_time = input("Enter start time for the appointment (HH:MM): ")
                end_time = input("Enter end time for the appointment (HH:MM): ")
                description = input("Enter description: ")
                self.AppointmentManager.select_appointment(date, start_time, end_time, description)
            elif choice == '3':
                year = self.get_int_input("Enter year: ")
                month = self.get_int_input("Enter month (1-12): ", 1, 12)
                self.AppointmentManager.display_calendar(year, month)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    def option_app(self):
        print(f"\nVeuillez indiquer votre age / poids / taille afin de calculer votre IMC")

    def ask_exercise_list(self):
        print(f"")
        exercice_list = get_muscles_list()
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
            print(f"Muscles associés à l'exercice ID {exercice_id} |  {exercice_nom[0][0]} :")
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