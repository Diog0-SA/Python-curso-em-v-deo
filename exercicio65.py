#média, maior e menor dentre os números digitados

contin='S'
soma=cont=menor=maior=0

while contin=='S':
    n=int(input('Digite um número: '))
    soma+=n
    cont+=1
    contin=str(input('Deseja continuar? [S] [N]')).upper().strip()[0]
    media= soma/cont
    if cont==1:
        menor=n
    if n>maior:
        maior=n
    if n<menor:
        menor=n

print('Foi digitado {} números, a média deles é {:.2f}, o menor número foi {} e o maior {}!' .format(cont, media, menor, maior))
