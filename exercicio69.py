idade=cont=maioridade=homem=mulheres20menos=0

while True:
    cont+=1
    sexo=continuar=' '
    idade=int(input(f'Quantos anos tem a {cont}° pessoa? '))
    while sexo not in 'MF':
        sexo=str(input(f'Qual o sexo da {cont}° pessoa? [F] [M] ')).upper() .strip() [0]
    if idade>18:
        maioridade+=1
    if sexo=='M':
        homem+=1
    if idade<20 and sexo=='F':
        mulheres20menos+=1
    while continuar not in 'SN':
        continuar=str(input('Deseja continuar? ')).upper() .strip() [0]
    if continuar=='N':
            break
print('=-'*12)
print(f'Foi contabilizado que {maioridade} tem mais de 18 anos. \nO número de homem registrados foi de {homem} \nPor fim. {mulheres20menos} mulheres tem menos de 20 anos')
print('Fim do programa.')
