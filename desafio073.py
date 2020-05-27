times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São-Paulo', 'Atlético-MG', 'Atlético-PR', 'Cruzeiro',
         'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'América-MG',
         'Sport', 'Vitória', 'Paraná')
print(f'\033[33mClassificação do Brasileirão 2018: {times}')
print(f'\033[34mOs 5 PRIMEIROS são: {times[:5]}')
print(f'\033[31mOs 4 ULTIMOS são: {times[-4:]}')
print(f'\033[32mClassificação por ordem ALFABÉTICA:{sorted(times)}')
print('\033[35mO time Chapecoense está na {}{}'.format(times.index('Chapecoense')+1, 'ª'))
