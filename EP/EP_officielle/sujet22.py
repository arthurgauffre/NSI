#exo 2

def crible(N):
    """
    Renvoie un tableau contenant tous les nombres premiers plus petits que N
    """
    premiers = []
    tab = [True] * N
    tab[0], tab[1] = False, False
    for i in range(..., N):
            if tab[i] == ...:
                premiers.append(...)
                for multiple in range(2*i, N, ...):
                    tab[multiple] = ...
    return premiers


assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]