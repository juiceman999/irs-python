import tkinter as tk
import mariadb

# Créer une fenêtre principale
root = tk.Tk()

# Faire la connexion à la base de données MariaDB
conn = mariadb.connect(user='your_username', password='your_password',
                       host='your_host', port=3306, database='your_database')

# Créer un menu principal
menu = tk.Menu(root)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Quitter", command=lambda: root.destroy())
menu.add_cascade(label="Fichier", menu=file_menu)
root.config(menu=menu)

# Ajouter une nouvelle entrée au menu
new_entry = tk.MenuEntry(root, text="Nouvelle entrée")
new_entry.grid(row=0, column=0)

# Définir une fonction pour ajouter la nouvelle entrée à la base de données
def add_to_db():
    # Récupérer le texte saisi dans l'entrée
    text = new_entry.get()

    # Exécuter une requête SQL pour ajouter le texte au tableau
    with conn.cursor() as cursor:
        query = "INSERT INTO tableau (text) VALUES (?)"
        data = (text,)
        cursor.execute(query, data)
        conn.commit()

# Ajouter une commande pour ajouter la nouvelle entrée au menu
add_to_db_command = tk.Button(root, text="Ajouter", command=add_to_db)
add_to_db_command.grid(row=0, column=1)

# Ajouter une commande pour fermer la fenêtre
quit_command = tk.Button(root, text="Quitter", command=lambda: root.destroy())
quit_command.grid(row=1, columnspan=2)

# Faire l'affichage du menu principal et de toutes les autres fenêtres
root.mainloop()