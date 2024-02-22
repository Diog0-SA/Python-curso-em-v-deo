f = str(input('Digite uma frase: ')).upper().strip()
print('Apareceram {} letras "A"' .format(f.count('A')))
print('A letra "A" apareceu pela primeira vez no {} caracter' .format(f.find('A')+1))
print('A letra "A" apareceu pela última vez na posição {}' .format(f.rfind('A')+1))