print('='*25)
print('Super Lojão de Minas')
print('='*25)
while True:
    nome = str(input('Qual é o nome do produto: '))
    valor = float(input('Qual é o valor do produto: R$'))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('-'*5, 'Fim do Programa', '-'*5)