# Análise dos números digitados 

cont=0
tupla=( int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))

print(tupla)
print(f'Você digitou os valores {tupla}')
print('-'*6)
print(f'O valor 9 aparece {tupla.count(9)} vezes')
print('-'*6)
if 3 in tupla:
    print(f'O valor 3 está na posição {tupla.index(3)+1}°')
else:
    print(f'O  valor 3 não foi digitado em nenhuma posição')
print('-'*6)
print(f'Os valores pares foram ', end=' ')
for n in tupla:
    if n%2==0:
        print(n, end=' ')
