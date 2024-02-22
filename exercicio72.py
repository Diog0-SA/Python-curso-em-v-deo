# zero ate vinte

atevinte= 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
n=21
continuar='S'
while continuar!='N':
    while True:
        n=int(input('Digite um número de 0 até 20: '))
        if n>20 or n<0:
            print('Erro! Tente novamente. ')
        else:
            print(f'O número {n} por extenso é: {atevinte[n]}')
            break
    continuar=str(input('Deseja continuar? [N] [S]')).upper().strip()[0]
    while continuar!='S' and continuar!='N':
        print('Desculpa não entendi')
        continuar=str(input('Deseja continuar? [N] [S]')).upper().strip()[0]
print('Fim')