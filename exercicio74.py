# cinco números aleatórios na tupla

from random import randint

tupla= (randint(1, 10), randint(1, 10), randint(1, 10),
randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram {tupla}')
print(f'O maior valor sorteado foi: {max(tupla)}')
print(f'O menor valor sorteado foi: {min(tupla)}')

#ou

'''
print(f'O maior valor sorteado foi {sorted(tupla)[4:]}')
print(f'O menor valor sorteado foi {sorted(tupla)[:1]}')
'''

