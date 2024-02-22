print('-=' *20)
print('Analisador de triângulos')
print('-=' *20)
r1=float(input('Escreva a primeira reta: '))
r2=float(input('Escreva a segunda reta: '))
r3=float(input('Escreva a terceira reta: '))
print('-' *40)

if r1< r2 + r3 and r2< r1+r3 and r3< r1+r2:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')
print('fim')