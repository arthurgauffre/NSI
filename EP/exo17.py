#exo 17.1

def indice_du_min(tab):
    min = ""
    for k in range(len(tab)-1) :  
        if tab[k] < tab[k+1]:
            min = k
    return min 
            
#exo 17.2

def separe(tab):
    i = 0
    j = len(tab) - 1 
    while i < j :
        if tab[i] == 0 :
            i = i + 1 
        else :
            tab[i], tab[j] = tab[j], tab[i]
            j = j - 1
    return tab