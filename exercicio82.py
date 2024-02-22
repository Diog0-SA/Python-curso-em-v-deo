# 3 listas, uma com todos os números, outra com os pares e outra com o ímpares

num=[]
par=[]
impar=[]
while True:
    num.append(int(input('Digite um número: ')))
    resp= str(input('Deseja continuar? [S] [N] '))
    if resp in 'Nn':
        break

for i, v in enumerate(num):
    if v%2==0:
        par.append(v)
    elif v%2==1:
        impar.append(v)
print('-=' *30)
print(f'A lista completa é {num} \nOs pares são {par} \nOs ímpares são {impar}')