import time
a = 0
b = 0
def crea_lst(n):
    return [0 for k in range(n)]

def crea_dict(n):
    return {k:0 for k in range(n)}

a = crea_lst(100)
b = crea_dict(100)

chrono1 = time.time()
if 0 in a:
    print("True")
temps1 = time.time() - chrono1

chrono2 = time.time()
if 0 in b:
    print("True")
temps2 = time.time() - chrono2

if temps1 > temps2:
    print('le dictionnaire est plus rapide', temps2, 'liste :', temps1)
else :
    print('la liste est plus rapide', temps1, 'dictionnaire :', temps2)