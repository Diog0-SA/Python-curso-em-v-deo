#salario com 15%

s=float(input('qual o salário do empregado? R$ '))
au=float(input('qual a porcentagem de aumento? '))
sc= s + (s*au/100)
print('o salário era R${:.2f}, e apartir de hoje vai ser R${:.2f} ' .format(s, sc))
