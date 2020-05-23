s = mil = menor = cont = barato = 0
print('='*40)
print('{:^40}'.format('Super Lojão de Minas'))
print('='*40)
while True:
    nome = str(input('Qual é o nome do produto: '))
    valor = float(input('Qual é o valor do produto: R$'))
    cont += 1
    s += valor
    if valor > 1000:
        mil += 1
    if cont == 1 or valor < menor:# o or precisa de uma premissa verdadeira, existindo uma ele executa o bloco
        menor = valor
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper()
    if resp == 'N':
        break
print('-'*5, 'Fim do Programa', '-'*5)
print(f'A soma dos valores dos proutos é R${s:.2f}')
print(f'Temos {mil} produtos que custam mais de R$1000.00')
print(f'O produto mais barato é {barato} e custa R${menor}')
