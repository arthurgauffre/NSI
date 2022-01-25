from queue import Queue

class Arbre:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

a = Arbre(8)
a.left = Arbre(4)
a.right = Arbre(5)
a.left.left = Arbre(2)
a.left.right = Arbre(1)
a.right.right = Arbre(3)

def bfs(arbre):
    file = Queue()
    file.put(arbre)
    sol = []
    while file.empty() is False :
        a = file.get()
        if a is not None :
            sol.append(a.data)
            file.put(a.left)
            file.put(a.right)
    return sol

print(bfs(a))