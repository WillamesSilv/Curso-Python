from datetime import date
anoatual = date.today().year
contmaior = 0
contmenor = 0
for ano in range(1, 8):
    nas = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(ano)))
    idade = anoatual - nas
    if idade >= 18:
        contmaior += 1
    else:
        contmenor += 1
print('{} pessoas são maior de idade e {} não são.'.format(contmaior, contmenor))

