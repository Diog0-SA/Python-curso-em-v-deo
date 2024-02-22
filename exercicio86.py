#matriz 3x3
'''
matriz=[[], [], []]
n=0

for c in range (1,10):
    n=int(input('Digite um valor: '))
    if c<=3:
        matriz[0].append(n)
    elif c<=6:
        matriz[1].append(n)
    elif c<=9:
        matriz[2].append(n)
print(f'{matriz[0]} \n{matriz[1]} \n{matriz[2]}')
'''

matriz=[[0, 0, 0],[0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite o valor da posição [{l} , {c}]: '))
print('=-' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()