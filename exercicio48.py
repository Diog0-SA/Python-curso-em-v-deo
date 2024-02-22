# soma de todos os números ímpares divisiveis por 3

s= 0
cont= 0
for c in range(1, 501, 2):
    if c%3==0:
        s= s+c
        cont= cont+1
print('A soma dos {} valores é {}' .format(cont, s))
