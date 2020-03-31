n1 = int(input('Qual é o primeiro número? '))
n2 = int(input('Qual é o segundo número? '))
n3 = int(input('Qual é o terceiro número? '))
# Verificando o menor número
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando o maior número
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
