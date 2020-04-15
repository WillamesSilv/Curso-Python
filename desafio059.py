n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
print('ATENÇÃO PARA AS OPÇÕES: \n[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA')
menu = int(input('Qual é sua escolha? '))
if menu == 1:
    print('A soma entre {} e {} é igual a {}'.format(n1, n2, n1 + n2))
