#some e mostre todos os números que o úsuario digitar. para no 999
'''
n=soma=cont=0

while n!=999:
    if n!=999:
        n=int(input('Digite um valor: '))
        soma= soma+n
        cont+=1
    if n==999:
        soma= soma-999
        cont-=1
print('Foi digitado {} e a soma deles é {}!' .format(cont, soma))
'''

# ou 

n=soma=cont=0
n=int(input('Digite um valor: '))

while n!=999:
    if n!=999:
        soma= soma+n
        cont+=1
        n=int(input('Digite um valor: '))
print('Foi digitado {} e a soma deles é {}!' .format(cont, soma))
