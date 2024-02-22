# nome e preço de vários produtos

baraton=' '
preco=total=maisdmil=baratop=cont=0

while True:
    cont+=1
    continuar=' '
    produto=str(input('Digite o nome do produto: ')).strip()
    preco=float(input(f'Qual é o preço do(a) {produto}? R$'))
    total+=preco
    if preco>1000:
        maisdmil+=1
    if cont==1:
        baraton=produto
        baratop=preco
    elif preco<baratop:
        baraton=produto
        baratop=preco
    while continuar not in 'SN':
        continuar=str(input('Deseja continuar? [S] [N]')).upper().strip()
    if continuar=='N':
        print('Fim da execução')
        print('=-'*12)
        break

print(f'O total foi de {total:.2f} \n{maisdmil} custam mais de R$1.000,00 \n{baraton} foi o produto mais barato custando R${baratop}.')
