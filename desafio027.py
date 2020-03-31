nome = str(input('Digite seu nome completo: ')).strip().split()
print('O seu primeiro nome é {}'.format(nome[0]))
print('O seu último nome é {}'.format(nome[len(nome)-1]))