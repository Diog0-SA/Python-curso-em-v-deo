# melhore o desafio 61

i= int(input('Digite o primeiro termo: '))
r= int(input('Digite a razão: '))
cont=0
mais=1
while cont<10:
    print(i, end='')
    print(' - ' if cont<9 else '',end='')
    i=i+r
    cont+=1

while mais!=0:
    mais=int(input('\nMais quantos termos deseja saber? '))
    cont=0
    while cont<mais:
        print(i, end='')
        print(' - ' if cont<mais-1 else ' ',end='')
        i=i+r
        cont+=1
print('Fim')
