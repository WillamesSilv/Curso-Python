n = soma = cont = med = maior = menor =0
r = 'S'
while r == 'S':#Podemos usar tbm o in 'Ss'. o in é em.
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()#strip() [0], para aceitar apenas a primeira letra
    if cont == 0:#Raciocinio logico, se um unico numero foi digitado, entao ele é o maior e o menor até o momento.
        maior = menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    cont += 1
    soma += n
med = soma / cont #Guanabara usou a média fora do laço, não se precisa calcular a media cada vez que digitar um núm
print('Você digitou:\n\033[32m{} Números, \033[33ma soma entre eles é {}.\n\033[34mA média é {:.1f}.'.format(cont, soma, med))
print('\033[35mO {} é o MAIOR.\n\033[36mO {} é o MENOR.'.format(maior, menor))
