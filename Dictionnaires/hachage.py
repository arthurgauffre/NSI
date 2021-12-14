import hashlib

lst = open("extraitrockyou.txt").read().splitlines()
dict = {}
for k in lst:
    dict[hashlib.md5(k.encode()).hexdigest()] = k

def inverse_md5(hash):
    if hash in dict:
        return dict[hash]
    return 'aucun mdp trouvé'

print(inverse_md5('0571749e2ac330a7455809c6b0e7af90'))







