#mega-sena

from random import randint
from time import sleep

print('-'*30)
print('      JOGA NA MEGA SENA')
print('-'*30)

lista=[]
cont=con=0

jogos=int(input('Quantos jogos deseja fazer? '))
while True:
    while True:
        num=randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >=6:
            break
    lista.sort()
    sleep(0.75)
    print(f'Jogo {con+1}: {lista}')
    lista.clear()
    cont=0
    con+=1
    if con==jogos:
        break
print('Boa sorte')
