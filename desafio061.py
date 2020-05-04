termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo - razao
c = 0
while c < 10:
    c += 1
    decimo += razao
    print('{}'.format(decimo), end=' - ')
print('fim')
'''Resolução do Guanabara, ele usou um termo = primeiro e um cont = 1
while cont <= 10:
    print('{} -'.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')'''