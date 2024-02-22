#nome e peso de várias pessoas

pessoas=[]
dados=[]
maior=menor=0
sn='s'

while True:
    if sn in 'Ss':
        pessoas.append(str(input('Nome: ')).strip())
        pessoas.append(float(input('Peso: ')))
        if len(dados)==0:
            maior=menor=pessoas[1]
        else:
            if pessoas[1] > maior:
                maior=pessoas[1]
            if pessoas[1] < menor:
                menor=pessoas[1]
        dados.append(pessoas[:])
        pessoas.clear()
        
    elif sn in 'Nn':
        break
    else:
        print('Desculpa não entendi, digite novamente')
    sn=str(input('Deseja continuar? [S] [N]'))

print('=-' *30)
print(f'{len(dados)} foram cadastradas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in dados:
    if p[1]==maior:
        print(p[0], end='-')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in dados:
    if p[1]==menor:
        print(p[0], end='-')
