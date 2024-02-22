# 7 anos de nascimento
from datetime import date 

maior= 0
menor= 0
for c in range(1, 8):
    ano= int(input('Digite o ano que a {}° pessoa nasceu: '.format(c)))
    if date.today().year-ano >= 21:
        maior=maior+1
    else:
        menor=menor+1
print('{} pessoas são maiores e {} são menores'.format(maior, menor))
