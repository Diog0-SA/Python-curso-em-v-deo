#par ou ímpar
'''
from random import choice

v=q=0
pi=''

while True:
    n=int(input('Diga um valor: '))
    pi=str(input('Par ou Ímpar? [P] [I] ')).strip() .upper()
    e= range(0, 10)
    c=choice(e)
    s=c+n
    if pi=='P' and s%2==0:
        print(f'jogador ganhou! Você escolheu {n} e o computador {c}, portanto deu {s} que é ÍMPAR')
        print('Vamos jogar novamente...')
        print('=-'*12)
        v+=1
        q+=1
    elif pi=='I' and s%2!=0:
        print(f'jogador ganhou! Você escolheu {n} e o computador {c}, portanto deu {s} que é PAR')
        print('Vamos jogar novamente...')
        print('=-'*12)
        v+=1
        q+=1
    else:
        q+=1
        print(f'Computador ganhou! Você escolheu {n} e o computador {c}, portanto deu {s}')
        print('Fim de jogo')
        break
print(f'Nós jogamos {q} vezes e você ganhou {v} vezes. Foi divertido!')
'''

from random import randint

v=0

while True:
    jogador=int(input('Diga um valor: '))
    computador=randint(0,10)
    total=jogador+computador
    tipo=' '
    while tipo not in 'PI':
        tipo=str(input('Par ou Ímpar? [P/I]')).strip() .upper() [0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR!' if total%2==0 else 'DEU ÍMPAR')
    if tipo=='P':
        if total%2==0:
            print('Você venceu!')
            v+=1
        else:
            print('Você perdeu!')
            break
    elif tipo=='I':
        if total%2==1:
            print('Você venceu!')
            v+=1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
