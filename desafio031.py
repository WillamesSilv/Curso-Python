viagem = float(input('Qual foi a distância percorrida em sua viagem? '))
if viagem <= 200:
    print('O valor cobrado por {}km percorridos é de R${:.2f}'.format(viagem, viagem * 0.5))
else:
    print('O valor cobrado por {}km percorridos é de R${:.2f}'.format(viagem, viagem * 0.45))