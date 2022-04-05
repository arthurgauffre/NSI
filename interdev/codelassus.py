def compare(prop, sol):
    n = len(prop)
    sol = list(sol)
    ver = ['_']*n
    for i in range(n):
        if prop[i] == sol[i]:
            ver[i] = 'R'
            sol[i] = '_'
    for i in range(n):
        if prop[i] in sol:
            ver[i] = 'J'
            k = sol.index(prop[i])
            sol[k] = '_'
    
    print(prop)
    print("".join(l for l in ver))
    
compare("MANOIR", "MAISON")