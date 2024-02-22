s=float(input('Qual o salário do funcionário? R$'))
if s>1250:
    ns=s+(s*10/100) #aumento de 10%
else:
    ns=s+(s*15/100) #aumento de 15%
print('Com o aumento salarial esse índividuo passa a receber R${:.2f}' .format(ns))