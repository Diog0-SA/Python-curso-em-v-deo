#5% de desconto

preço=float(input('qual é o preço do produto? '))
descon=float(input('qual é o desconto: '))
pf=preço-(preço*descon/100)
print('O produto custava R${}, na promoção com desconto de {:.2f}% vai custar {:.3f}' .format(preço, descon, pf))
