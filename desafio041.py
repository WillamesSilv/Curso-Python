from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print('O atleta que nasceu em {}, tem {} anos!'.format(nasc, idade))
if 0 < idade <= 9:
    print('Categoria MIRIM!')
elif idade <= 14:
    print('Categoria INFANTIL!')
elif idade <= 19:
    print('Categoria JUNIOR!')
elif idade <= 25:
    print('Categoria SÊNIOR!')
elif idade > 25:
    print('Categoria MASTER!')
