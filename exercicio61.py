# refaça o exercicio 51

t= int(input('Digite o primeiro termo: '))
r= int(input('Digite a razão: '))
cont=1

while cont<=10:
    print(t, end='')
    print('' if cont==10 else ' - ', end='')
    t=t+r
    cont+=1
print('\nfim')
