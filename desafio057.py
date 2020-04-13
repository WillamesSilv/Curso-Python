sexo = 0
s = str(input('Qual é o seu sexo [M/F]? ')).upper().strip()
if s != 'M' and s != 'F':
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Opção inválida, Digite [M/F]? ')).upper().strip()
        if sexo == 'M':
            print('Você digitou {}, portanto seu sexo é MASCULINO!'.format(sexo))
        if sexo == 'F':
            print('Você digitpu {}, portanto seu sexo é FEMININO!'.format(sexo))
if s == 'M':
    print('Você digitou {}, portanto seu sexo é MASCULINO!'.format(s))
if s == 'F':
    print('você digitou {}, portanto seu sexo é FEMININO!'.format(s))

