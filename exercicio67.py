#tabuada até o valor digitado for negativo

while True:
    t=int(input('Quer ver a tabuada de qual valor? '))
    if t<0:
        break
    for cont in range(0, 10):
        cont+=1
        z=t*cont
        print(f'{t} x {cont} = {z}')
    print('-=-'*12)
print('Programa encerrado.')
