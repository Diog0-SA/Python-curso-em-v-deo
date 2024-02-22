# desafio 20 ordem 

from random import shuffle
a1=input('Primeiro estudante: ')
a2=input('Segundo estudante: ')
a3=input('Terceiro estudante: ')
a4=input('Quarto estudante: ')
l=[a1, a2, a3, a4]
shuffle(l)
print('A ordem de apresentação é: {}'.format(l))