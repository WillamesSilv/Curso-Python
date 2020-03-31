print('\033[1;31m-=-' * 20)
print(' ' * 17,'Analisador de EMPRÉSTIMO!')
print('-=-' * 20)
casa = float(input('\033[mQual o valor do imóvel? R$'))
renda = float(input('Quanto é sua renda? R$'))
anos = int(input('Em quantos anos irá pagar? '))
prestação = (casa / anos) / 12
if prestação > (renda * 30 / 100):
    print('Seu empréstimo NÃO pode ser aprovado!')
else:
    print('Seu empréstimo foi APROVADO, o valor da parcela será de R${:.2f} mensal.'.format(prestação))
