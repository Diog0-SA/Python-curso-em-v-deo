#Ímpar e par
num=0
nume=[[], []]

for c in range(0,7):
    num=int(input(f'Digite o {c+1}º valor: '))
    if num%2==0:
        nume[0].append(num)
    else:
        nume[1].append(num)
nume[0].sort()
nume[1].sort()
print('=-'*30)
print(f'Os números pares foram: {nume[0]}')
print(f'\nOs números ímpares foram: {nume[1]}')

#tentei fazer como o exercicio 84, e não deu certo