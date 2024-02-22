# soma de seis números pares digitados

so= 0
for c in range(0,6):
    n= int(input('Digite um valor: '))
    if n%2==0:
        so+= n
print('A soma entre os números pares é: {}' .format(so))
