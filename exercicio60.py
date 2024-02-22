# número fatorial
'''
from math import factorial

n=int(input('Digite o número que deseja saber o fatorial: '))
f=factorial(n)
print('O fatorial de {} é {}.' .format(n, f))
'''
n=int(input('Digite o número que deseja saber o fatorial: '))
c=n
f=1
print('{} em fatorial=' .format(n), end=' ')
while c>0:
    print('{}' .format(c), end=' ')
    print(' . ' if c>1 else '= ' , end=' ')
    f*=c
    c-=1

print('{}' .format(f))