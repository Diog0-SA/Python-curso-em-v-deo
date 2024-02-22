#fibonacci

t=int(input('Quantos da sequência de fibonacci deseja saber? '))
t1=0
t2=1
print('{} - {} - '.format(t1, t2), end='')
cont=3

while cont<=t:
    t3=t1+t2
    print('{}' .format(t3), end='')
    print(' - ' if cont<t else '', end='')
    t1=t2
    t2=t3
    cont+=1
print('\nFim')
