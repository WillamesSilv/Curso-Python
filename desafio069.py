while True:
    print('='*25)
    print('CADASTRO DE PESSOAS')
    print('='*25)
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO: [M/F] ')).upper().strip()[0]
    print('-'*25)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('=' * 5, 'CADASTROS FINALIZADOS', '=' * 5)
