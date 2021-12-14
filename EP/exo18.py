# exo 18.1

def recherche(elt, tab):
    for k in range(len(tab)):
        if tab[k] == elt :
            return k
    return -1

# exo 18.2

def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(tab) - 1
    while a < tab[i] and i >= 0:
        l[i+1] = l[i]
        l[i] = a
        i = i - 1
    return l