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