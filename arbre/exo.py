class Arbre:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, sousarbre): # mutateur
        self.left = sousarbre

    def set_right(self, sousarbre): # mutateur
        self.right = sousarbre  

    def get_left(self): # accesseur
        return self.left

    def get_right(self): # accesseur
        return self.right

    def get_data(self): # accesseur
        return self.data

def prefixe(arbre):
    if arbre is None :
        return None
    print(arbre.data, end = '-')
    prefixe(arbre.left)
    prefixe(arbre.right)

def infixe(arbre):
    if arbre is None :
        return None
    infixe(arbre.left)
    print(arbre.data, end = '-')
    infixe(arbre.right)

def postfixe(arbre):
    if arbre is None :
        return None
    postfixe(arbre.left)
    postfixe(arbre.right)
    print(arbre.data, end = '-')

def taille(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + taille(arbre.left) + taille(arbre.right)

def hauteur(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + max(hauteur(arbre.left), hauteur(arbre.right))

def nbfeuilles(arbre):
    if arbre is None:
        return 0 
    if arbre.left is None and arbre.right is None:
        return 1
    else:
        return nbfeuilles(arbre.left) + nbfeuilles(arbre.right)

def recherche(arbre, n):
    if arbre is None:
        return False
    if arbre is n:
        return True 
    else:
        return recherche(arbre.left, n) or recherche(arbre.right, n)

# parcour infixe en interatif

def interativeinorder(arbre):
    s = []
    while (s != []) or (arbre != None):
        if arbre != None:
            s.append(arbre)
            arbre = arbre.left
        else:
            arbre = s.pop()
            print(arbre.data)
            arbre = arbre.right



a = Arbre(9)
a.left = Arbre(8)
a.right = Arbre(7)
a.left.left = Arbre(6)
a.left.right = Arbre(2)
print(taille(a))
print(recherche(a, 2))
print(recherche(a, 12))
print(interativeinorder(a), infixe(a))
