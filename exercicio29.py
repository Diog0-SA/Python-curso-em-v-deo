# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v=float(input('Em qual velocidade estava o carro? '))

if v>80:
    m= (v-80) *7
    print('Você recebeu uma multa por excesso de velociade. O Valor da multa foi de R${:.2f}' .format(m))
else:
    print('Você não recebeu multa alguma pois respeitou o limite de velocidade, continue assim!')
