"""

@author: Romain Hénon-Hilaire

"""

import argparse
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
        print(f"Démarrage mode graphique")
        gui_instance = GUI()
    else:
        print("This command is unavailable")

# Main guard
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Choisissez le mode de l'application.")
    parser.add_argument(
        "mode", 
        nargs='?', 
        choices=["Terminal", "GUI"], 
        default="Terminal", 
        help="Mode d'application à lancer (Terminal ou GUI)."
    )
    args = parser.parse_args()
    main(args.mode)
    #main("Terminal")
