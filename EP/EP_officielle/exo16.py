#exo1:

def maxi(tab):
    max = 0 
    indice_max = 0
    for chiffre in range(len(tab)):
        if tab[chiffre] > max:
            max = tab[chiffre]
            indice_max = chiffre
    return max, indice_max

print(maxi([1,5,6,9,1,2,3,7,9,8]))

# exo2:

def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2

print(positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]))  



