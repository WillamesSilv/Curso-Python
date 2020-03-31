vl = float(input('Qual é a velocidade do veículo? '))
print('>' * 7, end=' ')
print('\033[1;31mATENÇÃO VELOCIDADE MÁXIMA 80km/h', end=' ')
print('<' * 7)
if vl <= 80:
    print('\033[mVocê está dentro do limite de velocidade!')
else:
    print('\033[0;31;40mVocê ultrapassou o limite e foi multado em R$ {:.2f}\033[m'.format((vl-80) * 7.0))