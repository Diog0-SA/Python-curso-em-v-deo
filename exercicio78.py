menor=maior=n=0
lista=[]
for l in range(0,5):
    lista.append(int(input(f'Digite o valor da posição {l}: ')))
    if l==0:
        menor=maior=lista[l]
    else:
        if lista[l]>maior:
            maior=lista[l]
        if lista[l]<menor:
            menor=lista[l]

print('=-='*15)
print(f'Os valores digitados foram {lista}')
print(f'O menor valor foi {menor}, que estão nas posiçãos ', end='')
for i, v in enumerate(lista):
    if v==menor:
        print(f'{i}...', end='')
print()
print(f'O maior valor foi {maior}, que estão nas posiçãos ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()

#não terminado