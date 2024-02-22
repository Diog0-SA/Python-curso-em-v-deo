# alistamento militar
from datetime import date

ano= int(input('Em qual ano você nasceu? '))
idade= date.today().year - ano
falta=(ano + 18) - date.today().year

if idade < 18:
    print('Não chegou sua hora para se alistar.')
    print('Faltam {} anos para você se alistar.' .format(falta))
elif idade == 18:
    print('Este ano você precisa se alistar.')
elif idade > 18:
    falta= date.today().year - (ano + 18)
    print('Já passou da sua hora, você pagará uma multa ao se alistar.')
    print('Você já deveria ter se alistado há {} atrás.'.format(falta))
