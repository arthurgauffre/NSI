def puissance(x,n) : 
    if n == 0:   
        #"attention doit être positif"
        return 1 
    else : 
        return x * puissance(x,n-1)

print(puissance(2,3))


def pgcd(a,b) :
    if b == 0 : 
        return a
    else : 
        return pgcd(b, a%b)
    
print(pgcd(24,18))


def syracuse(n) : 
    if n == 1 : 
        return n
    if n%2 == 0 :
        print(n)
        return syracuse(n/2)        
    else : 
        return syracuse(n * 3 + 1) 
       
        
print(syracuse(47))

def recherche(lst,m): 
    if len(lst) == 1 : 
        if lst[0] == m : 
            return True
        else : 
            return False
    else :
        indice_milieu = len(lst)//2
        if lst[indice_milieu] <= m :
            lst = lst[indice_milieu:]
            return recherche(lst,m)
        else : 
            lst = lst[:indice_milieu]
            return recherche(lst,m)
        
print(recherche([1,2,3,4,5,6,7,8],4))




def puissance(x,n):
    if n == 0 :
        return 1
    if n%2 == 0 :
        return puissance(x*x,n/2)
    else :
        return x*puissance(x*x,(n-1)/2)

print(puissance(5,5))