# progressão aritmética

i= int(input('Digite o primeiro termo: '))
r= int(input('Digite a razão: '))
x= i+r*10
for c in range(i, x, r):
    print(c, end=' - ')
