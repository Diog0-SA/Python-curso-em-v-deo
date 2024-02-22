# caixa eletrônico
'''
n=cinquenta=vinte=dez=um=0
continuar=''
while True:
    n=0
    n=int(input('Qual será o valor sacado? R$'))
    if n>=50:
        cinquenta=n/50
        n=n%50
        print(f'\nTotal de {cinquenta:.0f} cédulas de R$50')
    if n>=20:
        vinte=n/20
        n=n%20
        print(f'\nTotal de {vinte:.0f} cédulas de R$20')
    if n>=10:
        dez=n/10
        n=n%10
        print(f'\nTotal de {dez:.0f} cédulas de R$10')
    if n>=1:
        um=n/1
        print(f'\nTotal de {um:.0f} cédulas de R$1')
    continuar=str(input('Deseja continuar? [N] [S] ')).upper() .strip()
    if continuar=='N':
        break
    print('=-='*13)
print('Fim')
'''
#ou 

valor=int(input('Que valo você quer sacar? R$'))
total=valor
ced=50
totced=0
while True:
    if total>=ced:
        total-=ced
        totced+=1
    else:
        if totced>0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        totced=0
        if total==0:
            break
print('Fim')