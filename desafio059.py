n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
menu = 1
while menu != 5:
    print('\033[33m=*=' * 10)
    print('\033[36mATENÇÃO PARA AS OPÇÕES: \n[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA')
    menu = int(input('\033[31mDigite o número da opção escolhida: '))
    if menu == 1:
        print('\033[32mA soma entre {} + {} é igual a {}\033[m'.format(n1, n2, n1 + n2))
    elif menu == 2:
        print('\033[33mMultiplicando os valores {} x {} é igual a {}.\033[m'.format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 > n2:
            maior = n1
            print('\033[34mEntre {} e {} o maior valor é {}.\033[m'.format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print('\033[34mEntre {} e {} o maior valor é {}.\033[m'.format(n1, n2, maior))
        else:
            print('\033[31mOs valores são IGUAIS.\033[m')
    elif menu == 4:
        print('\033[35mInforme os números novamente.\033[m')
        n1 = int(input('\033[36mDigite um número: '))
        n2 = int(input('Digite outro número: \033[m'))
    elif menu == 5:
        print('\033[31mFINALIZANDO...')
    else:
        print('Opção inválida, tente novamente!')
print('\033[34mObrigado, volte sempre!')
