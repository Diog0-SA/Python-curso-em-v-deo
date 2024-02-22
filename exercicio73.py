#os 20 primeiros colocados brasileirão

times= ('Palmeiras', 'Gremio', 'Atletico Mineiro',
'Flamengo', 'Botafogo', 'Red Bull Bragantino', 'Fluminense',
'CA Paranaense', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá',
'Corinthians', 'Cruzeiro', 'Vasco Gama', 'Bahia', 'Santos',
'Goiás', 'Coritiba', 'América')

print('Tabela do brasileirão')
print('-=='*10)
print(f'Os quatro primeiros são {times[:4]}')
print('-=='*10)
print(f'Os quatro últimos são {times[-4:]}')
print('-=='*10)
print(f'Times em ordem alfabéticas: {sorted(times)}')
print('-=='*10)
time=str(input('Qual time você deseja saber?'))
print('{} está na {}° posição' .format(time,times.index(time)+1))
print('Fim')
