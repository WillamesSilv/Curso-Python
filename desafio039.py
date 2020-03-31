import datetime
ano = int(input('Digite o ano do seu nascimento: '))
sexo = str(input('Qual é o sexo masculino ou feminino? ')).lower()
data = datetime.date.today().year - ano
print('Quem nasceu em {} tem {} ano(s).'.format(ano, data))
if sexo == 'feminino':
    print('Você não precisa se alistar!')
elif data < 18:
    print('Você não precisa se alistar, falta ainda {} ano(s).'.format(18 - data))
elif data == 18:
    print('Está na hora de se alistar!')
else:
    print('Já passou da hora de se alistar, deveria ser há {} ano(s) atrás.'.format(data - 18))
