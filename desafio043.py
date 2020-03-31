peso = float(input('Qual é o seu peso? (KGg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / altura ** 2
print('Considerando o peso {} e altura {}, seu IMC é {:.1f}'.format(peso, altura, imc))
if imc < 18.5:
    print('ABAIXO DO PESO!')
elif 18.5 > imc < 25:
    print('PESO IDEAL!')
elif 30 > imc >= 25:
    print('SOBRE PESO')
elif 40 > imc >=30:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA')
