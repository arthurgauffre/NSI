#exo 1

def renverse(mot):
    mot_renverse = ''
    for lettre in mot:
        mot_renverse = lettre + mot_renverse
    return mot_renverse
        
print(renverse("informatique"))

#exo 2

def crible(N):
    """
    Renvoie un tableau contenant tous les nombres premiers plus petits que N
    """
    premiers = []
    tab = [True] * N
    tab[0], tab[1] = False, False
    for i in range(2, N):
            if tab[i] == True:
                premiers.append(i)
                for multiple in range(2*i, N, i):
                    tab[multiple] = False
    return premiers

assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
print(crible(40))