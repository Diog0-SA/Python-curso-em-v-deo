# média de duas notas

n1= float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota: '))
m= (n1+n2)/2

if m < 5:
    print('A média é {:.1f}, portanto:\033[31mREPROVADO!\033[m'.format(m))
elif m >= 5 and m <= 6.9:
    print('A média é {:.1f}, portanto:\033[34mRECUPERAÇÃO!\033[m'.format(m))
elif m >= 7:
    print('A média é {:.1f}, portanto:\033[32mAPROVADO!\033[m'.format(m))