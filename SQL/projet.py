import sqlite3

#Connexion
connexion = sqlite3.connect('projet2.db')

#Récupération d'un curseur
c = connexion.cursor()

# ---- début des instructions SQL

#Création de la table
c.execute("""
    CREATE TABLE IF NOT EXISTS bulletin(
    Nom TEXT,
    Note INT);
    """)
while True:
    nom = input('nom :')




#Déconnexion
connexion.close()