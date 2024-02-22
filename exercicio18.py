#seno, cosseno, tangente
from math import radians,sin,cos,tan

a= float(input('Digite o valor do ângulo: '))
s=sin(radians(a))
c=cos(radians(a))
t=tan(radians(a))
print('O ângulo de {} tem o seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}' .format(a, s, c, t))
