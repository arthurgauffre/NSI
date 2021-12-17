# exo 6.1

def rendu(somme_a_rendre):
    n1, n2, n3 = 5, 2, 1
    nb1, nb2, nb3 = 0, 0, 0
    while somme_a_rendre != 0:
        while somme_a_rendre >= n1:
            somme_a_rendre -= n1
            nb1 += 1
        while somme_a_rendre >= n2 : 
            somme_a_rendre -= n2
            nb2 += 1
        if somme_a_rendre != 0:       
            somme_a_rendre -= n3
            nb3 += 1
    return nb1, nb2, nb3
        
print(rendu(14))
print(rendu(106))
print(rendu(13))

# exo 6.2 

class Maillon :
    def __init__(self,v) :
        self.valeur = v
        self.suivant = None

class File :
    def __init__(self) :
        self.dernier_file = None

    def enfile(self,element) :
        nouveau_maillon = Maillon(element)
        nouveau_maillon.suivant =  self.dernier_file
        self.dernier_file = nouveau_maillon

    def est_vide(self) :
        return self.dernier_file == None

    def affiche(self) :
        maillon = self.dernier_file
        while maillon != None :
            print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self) :
        if not self.est_vide() :
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.dernier_file
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = maillon.suivant.valeur
            maillon.suivant = None
            return resultat
        return None