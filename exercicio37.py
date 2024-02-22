# bases de conversão 

n= int(input('\033[1;35mDigite um número inteiro: \033[m'))
c= int(input('\033[1;35mPara qual base você quer converter?\033[m \033[1;36m Binário(1)\033[m / \033[1;32m octal(2)\033[m / \033[1;33m hexadecimal(3)\033[m '))
if c == 1:
    print('{} convertido para binário é: {}'.format(n, bin(n)[2:]))
elif c == 2:
    print('{} convertido para octal é: {}'.format(n, oct(n)[2:]))
elif c == 3:
    print('{} convertido para hexadecimal é: {}'.format(n, hex(n)[2:]))
else:
    print('\033[31mValor \033[30;41minválido!\033[m \033[31mPor favor tente novamente.\033[m')