import sys
import customtkinter as ctk
from app_gui_accueil import create_home_frame
from app_exercices import create_exercises_frame
from app_statistiques import create_stats_frame
from app_infos_personnelles import create_personal_info_frame
from app_user_management import load_user_info, save_user_info
from app import Applications
from app_login import login_with_gui, Utilisateur

class GUI(Applications):
    project_name = "Python GUI"
    project_version = float(1.0)

    def __init__(self):    
        self.terminal_state = "LOADING"
        self.user = None  # Initialiser l'utilisateur comme None
        self.launch_app()

    def launch_app(self):
        print(f"Welcome to the {GUI.project_name}")

        self.root = ctk.CTk()
        self.root.title("Application de Suivi Sportif")
        self.root.geometry("1024x768")

        # Empêcher la fermeture par défaut de la fenêtre
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Tentative de connexion
        self.authenticate_with_gui()

        # Si l'utilisateur est connecté, afficher l'interface principale
        if self.user:
            user_info = {"first_name": self.user.username}  # Adapter les données d'utilisateur si nécessaire
            self.frames = {
                "Accueil": create_home_frame(self.root, user_info),
                "Exercices": create_exercises_frame(self.root),
                "Statistiques": create_stats_frame(self.root),
                "Infos Personnelles": create_personal_info_frame(self.root, user_info),
            }

            for frame in self.frames.values():
                frame.pack_forget()

            self.create_nav_bar()
            self.show_frame("Accueil")
            self.root.mainloop()
        else:
            print("Authentication failed. Exiting the application.")
            sys.exit()

    def authenticate_with_gui(self):
        auth_window = ctk.CTkToplevel(self.root)
        auth_window.title("Login")
        auth_window.geometry("400x300")
        
        def attempt_login():
            username = username_entry.get()
            password = password_entry.get()
            user = login_with_gui(username, password)
            if user:
                self.user = user
                print(f"Successfully logged in as {self.user.username}.")
                auth_window.destroy()
            else:
                error_label.configure(text="Login failed. Please try again.")

        username_label = ctk.CTkLabel(auth_window, text="Username:")
        username_label.pack(pady=5)
        username_entry = ctk.CTkEntry(auth_window)
        username_entry.pack(pady=5)

        password_label = ctk.CTkLabel(auth_window, text="Password:")
        password_label.pack(pady=5)
        password_entry = ctk.CTkEntry(auth_window, show='*')
        password_entry.pack(pady=5)

        login_button = ctk.CTkButton(auth_window, text="Login", command=attempt_login)
        login_button.pack(pady=20)

        error_label = ctk.CTkLabel(auth_window, text="")
        error_label.pack(pady=5)

        auth_window.wait_window(auth_window)

    def create_nav_bar(self):
        nav_frame = ctk.CTkFrame(self.root)
        nav_frame.pack(side="top", fill="x")

        for name in self.frames:
            button = ctk.CTkButton(nav_frame, text=name, command=lambda n=name: self.show_frame(n))
            button.pack(side="left", padx=5, pady=5)

        # Ajout du bouton "Quitter"
        quit_button = ctk.CTkButton(nav_frame, text="Quitter", command=self.quit_app)
        quit_button.pack(side="right", padx=5, pady=5)

    def show_frame(self, name):
        for frame in self.frames.values():
            frame.pack_forget()
        frame = self.frames[name]
        frame.pack(fill="both", expand=True)

    def app_main_menu(self):
        print("Main menu\n 1) Start Game\n 2) Options\n 3) Quit Game")

    def planning_menu(self):
        pass

    def account_options_app(self):
        pass
    
    def ask_exercise_list(self):
        pass

    def ask_exercise_id(self):
        pass

    def quit_app(self):
        print("Quitting the application...")
        self.cleanup()
        sys.exit()

    def cleanup(self):
        print("Performing cleanup tasks...")
        #save_user_info({"first_name": "Utilisateur"})

    def on_closing(self):
        # Méthode appelée lorsque l'utilisateur tente de fermer la fenêtre
        # Empêche la fermeture par défaut et encourage l'utilisation du bouton Quitter
        print("Please use the Quit button to exit the application.")

if __name__ == "__main__":
    gui_instance = GUI()
