def hanoi(n, depart, inter, arrivee):
    """ n : nombre d'assiettes dans la pile
    # depart : la pile de départ("A", "B" ou "C")
    # inter : la pile intermédaire("A", "B" ou "C")
    # arrivee : la pile d'arrivée ("A", "B" ou "C") """

    if n == 1 :
        print(depart + " vers " + arrivee)
    else :
        hanoi(n-1, depart, arrivee, inter) 
        print(depart + " vers " + arrivee)
        hanoi(n-1, inter, depart, arrivee)

hanoi(5, "A", "B", "C")