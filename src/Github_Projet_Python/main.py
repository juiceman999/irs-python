import tkinter as tk
import customtkinter as ctk
from accueil import create_home_frame
from exercices import create_exercises_frame
from statistiques import create_stats_frame
from infos_personnelles import create_personal_info_frame
from user_management import load_user_info, save_user_info

def main():
    # Configurer l'interface graphique principale
    root = ctk.CTk()
    root.title("Application de Suivi Sportif")
    root.geometry("1024x768")

    user_info = load_user_info()

    # Vérifier si les informations utilisateur existent, sinon les demander
    if not user_info:
        # Logique pour demander les informations utilisateur
        user_info = {"first_name": "Utilisateur"}  # Temporaire pour l'exemple

    # Création des différentes vues
    frames = {
        "Accueil": create_home_frame(root, user_info),
        "Exercices": create_exercises_frame(root),
        "Statistiques": create_stats_frame(root),
        "Infos Personnelles": create_personal_info_frame(root, user_info),
    }

    for frame in frames.values():
        frame.pack_forget()

    def show_frame(name):
        for frame in frames.values():
            frame.pack_forget()
        frame = frames[name]
        frame.pack(fill="both", expand=True)

    # Barre de navigation
    nav_frame = ctk.CTkFrame(root)
    nav_frame.pack(side="top", fill="x")

    for name in frames:
        button = ctk.CTkButton(nav_frame, text=name, command=lambda n=name: show_frame(n))
        button.pack(side="left", padx=5, pady=5)

    show_frame("Accueil")
    
    root.mainloop()

if __name__ == "__main__":
    main()
