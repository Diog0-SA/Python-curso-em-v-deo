#leia 5 números e mostre-os em ordem sem usar o sort()

lista=[]
for c in range(0,5):
    n=int(input('Digite um valor: '))
    if c==0 or n>lista[len(lista)-1]:
        lista.append(n)
        print(f'Adicionado ao final da lista...')
    else:
        pos=0
        while pos < len(lista):
            if n<=lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos+=1
print('-=' *30)
print(f'Esses foram os números digitados em ordem - {lista}')

# n>lista[len(lista)-1] pegar o último elemento, também pode ser lista[-1]