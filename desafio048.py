soma = 0 #ACUMULADOR, A SOMA VAI COMEÇAR COM 0, OU SEJA, NENHUM NÚMERO DIVISIVEL POR 3
cont = 0 #ACUMULADOR, CONTADOR E VAI COMEÇAR A CONTAR A PARTIR DO 0
for c in range(1, 501, 2):
    if c % 3 == 0:
       cont = cont + 1 #O CONTADOR VAI CONTANDO OS VALORES, OU SEJA +1 QUE ACHOU.
       soma = soma + c #podemos simplificar por soma += c, soma recebe ele mesmo mais c.
print('A soma entre os {} valores executados é {}.'.format(cont, soma))
