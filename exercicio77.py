#tupla com varias palavras e mostre as vogais

tupla=('APRENDER', 'PROGRAMAR', 'LINGUAGEM ', 'PYTHON', 'CURSO',
        'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
        'PROGRAMADOR', 'FUTURO')

for p in tupla:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')