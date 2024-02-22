#preço com desconto dependendo da forma de pagamento

print('{:=^40}'.format('LOJAS ALGUMA COISA'))
preco= float(input('Qual o preço do produto? R$ '))
pag= int(input('Qual a forma de pagamento? [1] dinheiro ou cheque ou [2] cartão '))

if pag == 1:
    des=preco - preco*0.1 
elif pag == 2:
    x= int(input('Quantas vezes? '))
    if x == 1:
        des=preco - preco*0.05
    elif x == 2:
        des=preco
    elif x >= 3:
        des=preco*0.2 + preco
else:
    print('Valor inválido! Tente novamente.')

print('O valor do produto vai ser de R${:.2f} por R${:.2f}.' .format(preco,des))