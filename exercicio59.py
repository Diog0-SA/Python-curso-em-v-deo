# dois valores e um menu de opções

n1= int(input('Digite um valor: '))
n2= int(input('Digite outro valor: '))
menu=8

while menu!=5:
    menu=int(input('''Escolha uma opção:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR '''))
    print('=-='*15)
    if menu==1:
        soma=n1+n2
        print('A soma entre {} e {} é {}.' .format(n1, n2, soma))
    elif menu==2:
        multi=n1*n2
        print('A multiplicação entre {} e {} é {:.2f}.' .format(n1, n2, multi))
    elif menu==3:
        if n1 > n2:
            print('{} é maior que {}' .format(n1, n2))
        if n2 > n1: 
            print('{} é maior que {}' .format(n2, n1))
        if n2==n1:
            print('Os dois números são iguais!')
    elif menu==4:
        n1= float(input('Digite um valor: '))
        n2= float(input('Digite outro valor: '))
    elif menu==5:
        print('Fim')
    elif menu<0 or menu>5:
        print('Valor invalido, tente novamente')
