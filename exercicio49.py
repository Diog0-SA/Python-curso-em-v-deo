#tabuada com laço 'for'

'''n= int(input('Digite um número: '))
x=0
for c in range(1, 11):
    x= x+1
    r= n*x
    print('{} * {} = {}'.format(n, x, r))'''


# ou 

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} X {:2} = {}' .format(num, c, num*c))