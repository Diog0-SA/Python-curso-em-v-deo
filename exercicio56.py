# informaçoes de 4 pessoas

media=0
mvinte=0
velho=0
nv=''
for p in range(1, 5):
    print('-----{}° PESSOA-----'.format(p))
    nome= str(input('Digite o nome: ')).strip()
    idade= int(input('Digite a idade: '))
    sexo= str(input('Sexo [M/F]: ')).upper()
    media= media+idade
    if p==1 and sexo== 'M':
        velho=idade
        nv=nome
    elif sexo== 'M' and idade>velho:                        #HOMEM MAIS VELHO
        velho=idade
        nv=nome
    if sexo == 'F' and idade<20:                            # MULHERES MENOS DE 20 ANOS
        mvinte=mvinte+1
        
media=media/4
print('A média de idade do grupo é de {:.2f} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, nv))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mvinte))