#leia o sexo do úsuario

sexo=str(input('Digite seu sexo: [M] [F]')).strip().upper()[0]
while sexo not in 'mfMF':
    print('Valor incorreto! digite novamente.')
    sexo=str(input('Digite seu sexo: [M] [F]')).upper()
if sexo=='F':
    print('Sexo feminino registrado com sucesso!')
else:
    print('Sexo masculino registrado com sucesso!')
