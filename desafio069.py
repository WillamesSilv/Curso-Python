cont = h = f = 0
while True:
    print('='*25)
    print('CADASTRO DE PESSOAS')
    print('='*25)
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        f += 1
    print('-'*25)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('=' * 5, 'CADASTROS FINALIZADOS', '=' * 5)
print(f'Total de pessoas com 18 anos ou mais: {cont}')
print(f'Total de HOMENS cadastrados: {h}')
print(f'Total de MULHERES com menos de 20 anos: {f}')
