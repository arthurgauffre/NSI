from sympy.crypto.crypto import encipher_affine, decipher_affine
def rang(lettre):
    return ord(lettre) - 65

def affine(msg, a, b):
    mot = ''
    for lettre in msg:
        rg = rang(lettre)
        nv_rg = (a*rg +b)%26 
        nv_lettre = chr(nv_rg + 65)
        mot += nv_lettre
    return mot
        
def affine_sympy(msg, a, b):
    return encipher_affine(msg, (a, b))

msg = 'UCGXLODCMOXPMFMSRJCFQOGTCRSUSXC'
for k in range(20):
    for i in range(20):
        ct = decipher_affine(msg, k, i)
        if 'TRAVAIL' in ct:
            print(ct)


