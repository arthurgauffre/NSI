class Cellule :
    def __init__(self, contenu, lien):
        self.contenu = contenu
        self.lien = lien 

lst = Cellule(3, Cellule(5, Cellule(1,None)))
sauv_lien = lst.lien   
lst.suivante = Cellule(7, sauv_lien)
print(lst.lien.lien.contenu)