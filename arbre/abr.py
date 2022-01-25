from queue import Queue

class Arbre:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def infixe(arbre, s = None):
    if s is None:
        s = []
    if arbre is None :
        return None
    infixe(arbre.left, s)
    s.append(arbre.data)
    infixe(arbre.right, s)
    return s

def est_ABR(arbre):
    '''renvoie un booléen indiquant si arbre est un ABR'''
    parcours = infixe(arbre)
    return parcours == sorted(parcours) # on regarde si le parcours est égal au parcours trié 

def contient_valeur(arbre, valeur):
    if arbre is None :
        return False
    if arbre.data == valeur :
        return True
    if valeur < arbre.data :
        return contient_valeur(arbre.left, valeur)
    else:
        return contient_valeur(arbre.right, valeur)

def insertion(arbre, valeur):
    if arbre is None :
        return Arbre(valeur)
    else :
        v = arbre.data
        if valeur <= v :
            arbre.left = insertion(arbre.left, valeur)
        else:
            arbre.right = insertion(arbre.right, valeur)
        return arbre

# arbres-tests 

#arbre n°4
a = Arbre(5)
a.left = Arbre(2)
a.right = Arbre(7)
a.left.left = Arbre(0)
a.left.right = Arbre(3)
a.right.left = Arbre(6)
a.right.right = Arbre(8)

#arbre n°5
b = Arbre(3)
b.left = Arbre(2)
b.right = Arbre(5)
b.left.left = Arbre(1)
b.left.right = Arbre(9)
b.right.left = Arbre(4)
b.right.right = Arbre(6)

print(est_ABR(a))
print(est_ABR(b))
print(contient_valeur(a, 8))
print(contient_valeur(b, 8))