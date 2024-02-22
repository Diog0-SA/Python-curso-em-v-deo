d=int(input('Quantos dias ele foi alugado? '))
km=float(input('Quantos km rodados? '))
fv=60*d+0.15*km
print('O total a pagar é de R${:.2f}' .format(fv))