n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite um último número: '))
v = (n1, n2, n3, n4)
print('Você digitou os valores {}'.format(v))
print(f'O número 9 aparece {v.count(9)} vezes.')
if 3 not in v:
    print('O número 3 não foi digitado e não está em nenhuma posição.')
else:
    print(f'O número 3 está na posição {v.index(3)+1}ª.')
