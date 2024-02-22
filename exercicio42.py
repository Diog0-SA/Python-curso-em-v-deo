# acresentando o exercicio 35

print('-=' *20)
print('\033[35mAnalisador de triângulos\033[m')
print('-=' *20)
r1=float(input('Escreva a primeira reta: '))
r2=float(input('Escreva a segunda reta: '))
r3=float(input('Escreva a terceira reta: '))
print('-' *40)

if r1< r2 + r3 and r2< r1+r3 and r3< r1+r2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if r1==r2 and r2==r3 and r3==r1:
        print('EQUILÁTERO!')
    elif r1==r2 or r2==r3 or r3==r1:
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print('Os segmentos acima \033[31mNÃO\033[m podem formar um triângulo!')

print('fim')
