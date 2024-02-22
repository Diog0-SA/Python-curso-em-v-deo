from random import randint
from time import sleep

c= randint(0,5) #faz o computador "pensar"
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
j=int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2) #pausa para parecer que o computador está pensado
print('Você ganhou' if c==j else 'O computador ganhou')
print('Eu pensei em {}'.format(c))
