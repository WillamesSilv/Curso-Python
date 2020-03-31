salário = float(input('Qual é o valor do seu salário? R$'))
if salário <= 1250:
    aumento15 = (salário / 100 * 15)
    print('Você receberá um aumento de R${:.2f}'.format(aumento15))
    print('O seu salário que era R${:.2f}, passará a ser de R${:.2f}'.format(salário, salário + aumento15))
else:
    aumento10 = (salário / 100 * 10)
    print('Você receberá um aumento de R${:.2f}'.format(aumento10))
    print('O seu salário que era R${:.2f}, passará a ser de R${:.2f}'.format(salário, salário + aumento10))