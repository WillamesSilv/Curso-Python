num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('Analisando os números {} e {}, o número {} é maior.'.format(num1, num2, num1))
elif num2 > num1:
    print('Analisando os números {} e {}, o número {} é maior.'.format(num1, num2, num2))
else:
    print('Analisando os números, não existe valor maior os dois são iguais.'.format(num1, num2))

