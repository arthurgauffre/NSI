# exo 4.1

def moyenne (tab):
    moy = 0
    for k in range(len(tab)):
        moy += tab[k]
    return moy / len(tab)

assert moyenne([1]) == 1
assert moyenne([1,2,3,4,5,6,7]) == 4
assert moyenne([1,2]) == 1.5

# exo 4.2

def dichotomie(tab, x):
    """
    tab : tableau trié dans l’ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if len(tab) == 0:
        return False, 1
    # cas où x n'est pas compris entre les valeurs extrêmes
    if (x < tab[0]) or (x > tab[-1]):
        return False, 2
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = debut
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False, 3

print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],1))
print(dichotomie([],28))
