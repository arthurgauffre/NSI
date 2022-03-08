def interclassement(lst1, lst2):
    lst_totale = []
    i1 = 0 
    i2 = 0
    while i1 != len(lst1) and i2 != len(lst2):
        if lst1[i1] < lst2[i2]:
            lst_totale.append(lst1[i1])
            i1 += 1
        else:
            lst_totale.append(lst2[i2])
            i2 += 1
    return lst_totale + lst2[i2:] + lst1[i1:]

print(interclassement([2,5,7,12], [1,4,7,8,9]))

def tri_fusion(lst):
    if len(lst) <= 1:
        return lst
    else:
        m = len(lst) // 2
        return interclassement(tri_fusion(lst[:m]), tri_fusion(lst[m:]))
