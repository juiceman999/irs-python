"""
Objectif : Avoir 2 modes principaux 
   > un en ligne de commande
   > un en GUI : Panda3D / Custom Tkinter / Tkinter
Commencer par le terminal puuis alterner entre les 2
Avoir une classe abtraite pour l'application, une classe pour la CLI et une pour la GUI

Dispoer d'une base préparée avec les fichiers :
    - 
    - 
Configurer le fichier : database_config.py

"""

from app_cli import Terminal
from app_gui import GUI

def main(application_mode: str = "Terminal"):
    #match application_mode:
        #case "Terminal":
            #pass
        #case "Panda3D":
            #pass
        #case _:
            #print("This command is unavailable")

    if (application_mode == "Terminal"):
        print(f"Démarrage mode terminal")
        terminal_instance = Terminal()
    elif (application_mode == "GUI"):
        print(f"Démarrage mode terminal")
        terminal_instance = GUI()
    else:
        print("This command is unavailable")

# Main guard
if __name__ == "__main__":
    main("Terminal")
