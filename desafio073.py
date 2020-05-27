times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São-Paulo', 'Atlético-MG', 'Atlético-PR', 'Cruzeiro',
         'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'América-MG',
         'Sport', 'Vitória', 'Paraná')
print(f'Classificação do Brasileirão 2018: {times}')
print(f'Os 5 PRIMEIROS são: {times[:5]}')
print(f'Os 4 ULTIMOS são: {times[-4:]}')
print(f'Classificação por ordem ALFABÉTICA:{sorted(times)}')
print('O time Chapecoense está na {}{}'.format(times.index('Chapecoense')+1, 'ª'))
