# empréstimo bancário

casa= float(input('\033[35;47mQual o valor da casa escolhida? R$ \033[m'))
sal= float(input('\033[35;47mQual é o seu salário? R$ \033[m'))
tempo= int(input('\033[35;47mEm quantos anos você pretende pagar? \033[m'))
print('\033[7;35;47m-=-\033[m'*20)
#informações necessárias
porc=sal*30/100
re= casa/(tempo*12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(casa, tempo, re))
if re > porc:
    print('Empréstimo negado')
else:
    print('Empréstimo liberado')
#calculo
