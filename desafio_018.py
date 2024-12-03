import math
from math import radians, sin, cos, tan

angulo = float(input("Digite o ângulo em graus: "))
angulo_rad = radians(angulo)
seno = sin(angulo_rad)
cosseno = cos(angulo_rad)
tangente = tan(angulo_rad)

print("Para um ângulo de {} graus, o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}".format(angulo, seno, cosseno, tangente))

#outra forma de resolver
#seno = sin(radians(angulo))
#cosseno = cos(radians(angulo))
#tangente = tan(radians(angulo))

