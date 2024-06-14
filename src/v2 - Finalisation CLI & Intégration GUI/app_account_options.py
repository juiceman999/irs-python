# account_options.py

from tabulate import tabulate
from app_query import delete_account, save_health_data, get_health_data, save_personal_stats, get_personal_stats

class AccountOptions:
    def __init__(self, username):
        self.username = username
    """
    def display_menu(self):
        while True:
            print("""
    """
Account Options Menu:
    1) Delete current account
    2) Health Menu
    3) Personal Stats Menu
    4) Back to previous menu
    """
    """)
            choice = input("Please enter your choice (1-4): ")
            if choice == '1':
                self.delete_account()
            elif choice == '2':
                self.health_menu()
            elif choice == '3':
                self.personal_stats_menu()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
    """
    def delete_account(self):
        confirm = input("Are you sure you want to delete your account? (yes/no): ")
        if confirm.lower() == 'yes':
            delete_account(self.username)
            print("Account deleted successfully.")
            exit()  # Exit the application after account deletion

    def health_menu(self):
        while True:
            print("""
Health Menu:
    1) Enter health data
    2) View latest health data
    3) Back to account options menu
            """)
            choice = input("Please enter your choice (1-3): ")
            if choice == '1':
                self.enter_health_data()
            elif choice == '2':
                self.view_health_data()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

    def enter_health_data(self):
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (cm): "))
        birthdate = input("Enter birthdate (YYYY-MM-DD): ")
        sex = input("Enter sex (M/F): ")
        goal = input("Enter goal (Weight loss/Mass gain): ").lower() in ['weight loss', 'mass gain']

        save_health_data(self.username, weight, height, birthdate, sex, goal)
        print("Health data saved successfully.")

    def view_health_data(self):
        stats = get_health_data(self.username)
        if stats:
            print("\nHistorique des données de santé de", self.username ,":")
            headers = ["Timestamp", "Poids (Kg)", "Taille (cm)", "Date de naissance", "Sex", "Goal"]
            table = [[stat[-1], stat[2], stat[3], stat[4], stat[5], stat[6]] for stat in stats]
            print(tabulate(table, headers, tablefmt="grid"))
        else:
            print("No personal stats found.")

    def personal_stats_menu(self):
        while True:
            print("""
Personal Stats Menu:
    1) Enter personal stats
    2) View personal stats history
    3) Back to account options menu
            """)
            choice = input("Please enter your choice (1-3): ")
            if choice == '1':
                self.enter_personal_stats()
            elif choice == '2':
                self.view_personal_stats_history()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

    def enter_personal_stats(self):
        stats = {
            'neck': float(input("Enter neck circumference (cm): ")),
            'chest': float(input("Enter chest circumference (cm): ")),
            'waist': float(input("Enter waist circumference (cm): ")),
            'hips': float(input("Enter hips circumference (cm): ")),
            'thigh': float(input("Enter thigh circumference (cm): ")),
            'calf': float(input("Enter calf circumference (cm): ")),
            'biceps': float(input("Enter biceps circumference (cm): ")),
            'forearm': float(input("Enter forearm circumference (cm): ")),
            'wrist': float(input("Enter wrist circumference (cm): ")),
            'shoulders': float(input("Enter shoulders circumference (cm): "))
        }
        save_personal_stats(self.username, **stats)
        print("Personal stats saved successfully.")

    def view_personal_stats_history(self):
        stats = get_personal_stats(self.username)
        if stats:
            print("\nPersonal Stats History of", self.username ,":")
            headers = ["Timestamp", "Neck (cm)", "Chest (cm)", "Waist (cm)", "Hips (cm)", "Thigh (cm)", "Calf (cm)", "Biceps (cm)", "Forearm (cm)", "Wrist (cm)", "Shoulders (cm)"]
            table = [[stat[-1], stat[2], stat[3], stat[4], stat[5], stat[6], stat[7], stat[8], stat[9], stat[10], stat[11]] for stat in stats]
            print(tabulate(table, headers, tablefmt="grid"))
        else:
            print("No personal stats found.")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
