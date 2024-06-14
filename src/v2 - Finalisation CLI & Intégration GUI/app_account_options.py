from tabulate import tabulate
from app_query import delete_account, save_health_data, get_health_data, save_personal_stats, get_personal_stats

class AccountOptions:
    def __init__(self, username):
        self.username = username

    def display_menu(self):
        while True:
            print("""
Menu Options du Compte :
    1) Supprimer le compte actuel
    2) Menu Santé
    3) Menu Statistiques Personnelles
    4) Retour au menu précédent
            """)
            choice = input("Veuillez entrer votre choix (1-4) : ")
            if choice == '1':
                self.delete_account()
            elif choice == '2':
                self.health_menu()
            elif choice == '3':
                self.personal_stats_menu()
            elif choice == '4':
                break
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")

    def delete_account(self):
        confirm = input("Êtes-vous sûr de vouloir supprimer votre compte ? (oui/non) : ")
        if confirm.lower() == 'oui':
            delete_account(self.username)
            print("Compte supprimé avec succès.")
            exit()  # Quitte l'application après la suppression du compte

    def health_menu(self):
        while True:
            print("""
Menu Santé :
    1) Entrer les données de santé
    2) Voir les dernières données de santé
    3) Retour au menu des options du compte
            """)
            choice = input("Veuillez entrer votre choix (1-3) : ")
            if choice == '1':
                self.enter_health_data()
            elif choice == '2':
                self.view_health_data()
            elif choice == '3':
                break
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 1 et 3.")

    def enter_health_data(self):
        weight = float(input("Entrez le poids (kg) : "))
        height = float(input("Entrez la taille (cm) : "))
        goal = input("Entrez l'objectif (Perte de poids/Gain de masse) : ").lower() in ['perte de poids', 'gain de masse']

        save_health_data(self.username, weight, height, goal)
        print("Données de santé enregistrées avec succès.")

    def view_health_data(self):
        stats = get_health_data(self.username)
        if stats:
            print("\nHistorique des données de santé de", self.username, ":")
            headers = ["Horodatage", "Poids (Kg)", "Taille (cm)", "Objectif"]
            table = [[stat[-1], stat[2], stat[3], stat[4]] for stat in stats]
            print(tabulate(table, headers, tablefmt="grid"))
        else:
            print("Aucune donnée personnelle trouvée.")

    def personal_stats_menu(self):
        while True:
            print("""
Menu Statistiques Personnelles :
    1) Entrer des statistiques personnelles
    2) Voir l'historique des statistiques personnelles
    3) Retour au menu des options du compte
            """)
            choice = input("Veuillez entrer votre choix (1-3) : ")
            if choice == '1':
                self.enter_personal_stats()
            elif choice == '2':
                self.view_personal_stats_history()
            elif choice == '3':
                break
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 1 et 3.")

    def enter_personal_stats(self):
        stats = {
            'neck': float(input("Entrez la circonférence du cou (cm) : ")),
            'chest': float(input("Entrez la circonférence de la poitrine (cm) : ")),
            'waist': float(input("Entrez la circonférence de la taille (cm) : ")),
            'hips': float(input("Entrez la circonférence des hanches (cm) : ")),
            'thigh': float(input("Entrez la circonférence de la cuisse (cm) : ")),
            'calf': float(input("Entrez la circonférence du mollet (cm) : ")),
            'biceps': float(input("Entrez la circonférence du biceps (cm) : ")),
            'forearm': float(input("Entrez la circonférence de l'avant-bras (cm) : ")),
            'wrist': float(input("Entrez la circonférence du poignet (cm) : ")),
            'shoulders': float(input("Entrez la circonférence des épaules (cm) : "))
        }
        save_personal_stats(self.username, **stats)
        print("Statistiques personnelles enregistrées avec succès.")

    def view_personal_stats_history(self):
        stats = get_personal_stats(self.username)
        if stats:
            print("\nHistorique des statistiques personnelles de", self.username, ":")
            headers = ["Horodatage", "Cou (cm)", "Poitrine (cm)", "Taille (cm)", "Hanches (cm)", "Cuisse (cm)", "Mollet (cm)", "Biceps (cm)", "Avant-bras (cm)", "Poignet (cm)", "Épaules (cm)"]
            table = [[stat[-1], stat[2], stat[3], stat[4], stat[5], stat[6], stat[7], stat[8], stat[9], stat[10], stat[11]] for stat in stats]
            print(tabulate(table, headers, tablefmt="grid"))
        else:
            print("Aucune statistique personnelle trouvée.")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Sous-poids"
        elif 18.5 <= bmi < 24.9:
            return "Poids normal"
        elif 25 <= bmi < 29.9:
            return "Surpoids"
