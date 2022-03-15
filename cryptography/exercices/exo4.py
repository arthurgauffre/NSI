import Crypto
import libnum
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Random import get_random_bytes 

p = 2**521-1
q = 2**607-1
n = p * q
phi = (p - 1) * (q - 1)

e = 65537  # 65537 est un nombre premier, donc forcément premier avec phi
d = libnum.invmod(e, phi)  # on calcule l'inverse de e modulo phi

M = 44528752388922004335673733938967390739786061339673400314583577394237347689573

c = pow(M, e, n) # M puissance e modulo n
res = pow(c, d, n)

print(long_to_bytes(res))