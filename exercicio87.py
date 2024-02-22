#aprimore a matriz

matriz=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma=terceira=segunda=0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite o valor da posição [{l}, {c}]: '))
#                                                                            Guardando os números
        if matriz[l][c]%2==0:
            soma+=matriz[l][c]
#                                                                            Verificando se é par e somando
        if c==2:
            terceira+=matriz[l][c]
#                                                                            Verificando se é da 3ª coluna e somando
for c in range(0,3):
    if c==0:
        segunda=matriz[1][c]
    elif matriz[1][c]>segunda:
        segunda=matriz[1][c]
#                                                                         Fazendo um for para ver todos os elementos da linha 1 e vendo o maior
print('=-' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
#                                                                           Print estilizado
print(f'A soma dos pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {terceira}.')
print(f'O maior valor da segunda linha é {segunda}.')