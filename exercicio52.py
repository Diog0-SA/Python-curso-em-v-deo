# número primo

n= int(input('digite um número: '))
total=0
for c in range(1, n+1):
    r=n/c
    if r%1==0 or r%n==0:
        print('\033[33m{}\033[m'.format(c), end=' - ')
        total+=1
    else:
        print('\033[31m{}\033[m'.format(c), end=' - ')
if total==2:
    print('\nÉ um número primo')
else:
    print('\nO número não é primo')
