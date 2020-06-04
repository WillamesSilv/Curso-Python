núm = (int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite um último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O número 9 aparece {núm.count(9)} vezes.')
if 3 not in núm:
    print('O número 3 não foi digitado e não está em nenhuma posição.')
else:
    print(f'O número 3 está na {núm.index(3)+1}ª posição.')
print('Os valores pares digitados foram os números', end= ' ')
for par in núm:
  if  par % 2 == 0:
    print(par, end=' ')
