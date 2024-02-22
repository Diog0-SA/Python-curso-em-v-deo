d=float(input('Qual a distância em km da sua viagem? '))
'''if d<=200:
    p=d*0.50
else: 
    p=d*0.45
print('Sua passagem de {} km, fica pelo preço de R${:.2f}' .format(d,p))

jeito longo de fazer'''

p=d*0.50 if d<=200 else d*0.45
print('Sua passagem de {} km, fica pelo preço de R${:.2f}' .format(d,p))

# jeito 'simplificado'
