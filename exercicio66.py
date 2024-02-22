#vario números digitados ate 999

s=cont=0

while True:
    n=int(input('Digite um número(999 para parar): '))
    if n==999:
        break
    cont+=1
    s+=n
print(f'Foi digitado {cont} números e a soma dos valores foi {s}')