import mysql.connector
mysql.connector.Connect
# Connexion à la base de données
conn = mysql.connector.connect(
    host='192.168.118.145',  # Remplacez par l'adresse de votre serveur MySQL
    user='admin',       # Remplacez par votre nom d'utilisateur MySQL
    password='MotDePasse999!',  # Remplacez par votre mot de passe MySQL          WFChFVZ7Zj@M!K6Bap%rf624v^oxAv@N
    database='gym'
)

# Création d'un curseur
cursor = conn.cursor()

exercice_id = input("Choisissez l'exercice : ")

# Exercice ID pour lequel on veut voir les muscles associés
##exercice_id = 5

# Requête SQL pour récupérer les muscles associés à un exercice
query_me = """
SELECT m.id, m.nom
FROM muscles m
JOIN exercice_muscle em ON m.id = em.muscle_id
WHERE em.exercice_id = %s
"""

# Requête SQL pour récupérer les muscles associés à un exercice
query_eid = """
SELECT e.nom
FROM exercices e
WHERE e.id = %s
"""

# Exécution de la requête
cursor.execute(query_me, (exercice_id,))
# Récupération des résultats
muscles = cursor.fetchall()

# Exécution de la requête
cursor.execute(query_eid, (exercice_id,))
# Récupération des résultats
exercice_nom = cursor.fetchall()

# Affichage des résultats
print(f"Muscles associés à l'exercice ID {exercice_id} |-->  {exercice_nom[0][0]} :")
for muscle in muscles:
    print(f"ID: {muscle[0]}, Nom: {muscle[1]}")

# Fermeture du curseur et de la connexion
cursor.close()
conn.close()
