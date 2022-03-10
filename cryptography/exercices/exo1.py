from sympy.crypto.crypto import encipher_shift, decipher_shift
msg = 'RYTVJKGCLJWRTZCVRMVTLEDFULCVHLZWRZKKFLKRMFKIVGCRTV'
for k in range(1, 27):
    ct = decipher_shift(msg, k)
    if 'FACILE' in ct:
        print(ct)
