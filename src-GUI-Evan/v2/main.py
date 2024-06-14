import argparse
from .app_cli import Terminal
from .app_gui import main_gui

def main(application_mode: str = "Terminal"):
    if application_mode == "Terminal":
        print("Démarrage mode terminal")
        terminal_instance = Terminal()
    elif application_mode == "GUI":
        print("Démarrage mode graphique")
        main_gui()
    else:
        print("This command is unavailable")

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
