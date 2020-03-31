from random import choice
pa = input('Primeiro aluno: ')
sa = input('Segundo aluno: ')
ta = input('Terceiro aluno: ')
qa = input('Quarto aluno: ')
ae = choice([pa, sa, ta, qa])
print('O aluno escolhido foi {}.'.format(ae))
