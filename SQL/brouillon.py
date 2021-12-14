import sqlite3

connexion = sqlite3.connect('mynewbase.db')
c = connexion.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS bulletin(
    Nom TEXT,
    Note INT);
    """)

connexion.commit()

def menu():
    print("Menu")
    print("1. Saisir des notes")
    print("2. Consulter les notes")
    print("3. Quitter")

def saisie():
    while True :
        nom = input("Nom ?")
        if nom == 'q' or nom == 'Q':
            break
        note = input("Note ?")
        data = (nom, note)
        c.execute('''INSERT INTO bulletin VALUES (?,?)''', data)

def consultation(nom_note):
    c.execute("SELECT Note FROM Bulletin WHERE Nom = ?", nom_note)
    print(c.fetchall())  
    

menu()
choix = ""


while True:
    choix = int(input("Choix ?"))
    if choix == 1:       
        saisie()    
    if choix == 2:
        consultation(input("Nom ?"))
    if choix == 3:
        break

connexion.close()