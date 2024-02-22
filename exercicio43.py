#imc

peso= float(input('Qual é o seu peso?(Kg) '))
altura= float(input('Qual é a sua altura?(em metros) '))
imc= peso / (altura * altura)

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc <= 25:
    print('PESO IDEAL')
elif imc > 25 and imc <= 30:
    print('SOBREPESO')
elif imc > 30 and imc <= 40:
    print('OBESO')
elif imc > 40:
    print('OBESIDADE MÓRBIDA')