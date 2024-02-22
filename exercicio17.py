from math import sqrt

co= float(input('Digite o valor do cateto oposto: '))
ca= float(input('Digite o valor do cateto adjecente: '))
h=co**2 + ca**2
h= sqrt(h)
print('A hipotenusa é: {}' .format(h)) 