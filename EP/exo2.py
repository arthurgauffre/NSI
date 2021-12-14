# exo 2.1

def moyenne(tab):
    moy = 0
    for k in range(len(tab)):
        moy += tab[k]
    if len(tab) == 0 :
        return "erreur"
    return moy / len(tab)

print(moyenne([5,3,8]))
print(moyenne([1,2,3,4,5,6,7,8,9,10]))
print(moyenne([]))

# exo 2.2

def tri(tab):
    #i est le premier indice de la zone non triee, j le dernier indice.
    #Au debut, la zone non triee est le tableau entier.
    i = 0
    j = len(tab) - 1
    while i != j :
        if tab[i]== 0:
            i = i + 1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j = j - 1
    return tab

print(tri([0,1,0,1,0,1,0,1,0]))