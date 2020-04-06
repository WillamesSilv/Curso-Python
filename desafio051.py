termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razao #regra da PA para o decimo termo, se fosseo vigesimo colaria 20 no lugar do (10 - 1)
for c in range(termo, decimo+razao, razao):
    print('{}'.format(c), end=' - ')
print('fim')
