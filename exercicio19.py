from random import choice

a1= input('Digite o nome do aluno 1: ')
a2= input('Digite o nome do aluno 2: ')
a3= input('Digite o nome do aluno 3: ')
a4= input('Digite o nome do aluno 4: ')
l=[a1, a2, a3, a4]
r=choice(l)
print('o aluno(a) escolhido(a) foi {}!' .format(r))  