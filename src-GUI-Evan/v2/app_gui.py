import os
import sys
import customtkinter as ctk
from app import Applications
from accueil import create_home_frame
from exercices import create_exercises_frame
from statistiques import create_stats_frame
from infos_personnelles import create_personal_info_frame
from user_management import load_user_info, save_user_info

class GUI(Applications):
    project_name = "Python GUI"
    project_version = float(1.0)

    def __init__(self):
        self.terminal_state = "LOADING"
        self.launch_app()

    def launch_app(self):
        self.clear_terminal()
        print(f"Welcome to the {GUI.project_name}")

        self.root = ctk.CTk()
        self.root.title("Application de Suivi Sportif")
        self.root.geometry("1024x768")

        user_info = load_user_info()
        if not user_info:
            user_info = {"first_name": "Utilisateur"}

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

    def create_nav_bar(self):
        nav_frame = ctk.CTkFrame(self.root)
        nav_frame.pack(side="top", fill="x")

        for name in self.frames:
            button = ctk.CTkButton(nav_frame, text=name, command=lambda n=name: self.show_frame(n))
            button.pack(side="left", padx=5, pady=5)

    def show_frame(self, name):
        for frame in self.frames.values():
            frame.pack_forget()
        frame = self.frames[name]
        frame.pack(fill="both", expand=True)

    def app_main_menu(self):
        pass

    def planning_menu(self):
        pass

    def account_options_app(self):
        pass

    def ask_exercise_list(self):
        pass

    def ask_exercise_id(self):
        pass

    def quit_app(self):
        self.root.quit()

    def clear_terminal(self):
        if sys.platform == "win32":
            os.system('cls')
        elif sys.platform == 'darwin':
            os.system('clear')
        else:
            os.system('cls')

def main_gui():
    GUI()
