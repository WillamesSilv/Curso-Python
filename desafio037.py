print('\033[1;32m*' * 30)
print(' ''CONVERSOR DE BASES NUMÉRICAS')
print('*' * 30)
numero = int(input('\033[mDigite um número inteiro: '))
print('''Escolha uma das bases para conversão:
1 - Conversão para BINÁRIO;
2 - Conversão para OCTAL;
3 - Conversão para HEXADECIMAL.''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número {} convertido para BINÁRIO é igual a {}.'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O número {} convertido para OCTAL é igual a {}.'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}.'.format(numero, hex(numero)[2:]))
else:
    print('Opção INVÁLIDA, escolha 1, 2 ou 3 e tente novamente!')
