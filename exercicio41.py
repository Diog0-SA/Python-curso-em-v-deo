#categorias natação
from datetime import date

ano = int(input('Qual o ano de nascimento? '))
idade=date.today().year - ano
print('A pessoa tem {} anos.'.format(idade))

if idade <= 9:
    print('MIRIM')
elif idade <=14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')
