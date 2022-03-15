import Crypto
import libnum
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Random import get_random_bytes 

bits = 2048
msg = "en NSI on fait de la crypto"

p = Crypto.Util.number.getPrime(bits, randfunc=get_random_bytes)
q = Crypto.Util.number.getPrime(bits, randfunc=get_random_bytes)

n = p * q
phi = (p - 1) * (q - 1)

e = 65537  # 65537 est un nombre premier, donc forcément premier avec phi
d = libnum.invmod(e, phi)  # on calcule l'inverse de e modulo phi

M = bytes_to_long(msg.encode('utf-8'))

c = pow(M, e, n) # M puissance e modulo n
res = pow(c, d, n)

print(long_to_bytes(res))