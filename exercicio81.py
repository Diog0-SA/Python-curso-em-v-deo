# leia vários números e mostre: Quantos números foram adicionados, ordem decrescente e se o valor 5 foi digitado

lista=[]
continuar='S'
cinco=0
while True:
    if continuar=='S':
        n=lista.append(int(input('Digite um número: ')))
    elif continuar=='N':
        break
    else:
        while continuar!='S' and continuar!='N':
            print('Desculpa não entendi, digite novamente')
            continuar=str(input('Deseja continuar? [S] [N]')).upper() .strip() [0]
    continuar=str(input('Deseja continuar? [S] [N]')).upper() .strip() [0]
tras=lista[:]
tras.sort(reverse=True)
print('-='*30)
print(f'Foram digitados {len(lista)} números, e eles são: {lista} \nEm ordem decrescente fica {tras}')
if 5 in lista:
    print(f'O número 5 (cinco) foi digitado na lista')
else:
    print('O número 5 (cinco) não foi digitado na lista')
