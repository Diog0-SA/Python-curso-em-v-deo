#nome e duas notas de alunos, lista composta

ficha=[]
continuar='s'

while True:
    if continuar in 'Ss':
        n=str(input('Nome: '))
        n1=float(input('Nota 1: '))
        n2=float(input('Nota 2: '))
        m=(n1+n2) / 2
        ficha.append([n, [n1,n2], m])
    elif continuar in 'Nn':
        break
    else:
        print('Desculpa não entendi. Tente novamente.')
    continuar=str(input('Deseja continuar? [S] [N] ')).strip() [0]
print('=-'*30)
print(f'{"No.":<4}{"NOME:":<10}{"MÉDIA:":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('=-'*30)
    opc= int(input('Mostrar notas de qual estudante? (999 interrempe): '))
    if opc ==999:
        print('Finalizando...')
        break
    if opc<= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('Fim')
