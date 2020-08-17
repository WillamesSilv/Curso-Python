listagem = ('Aroz', 15.80, 'Feijão', 5.40, 'Óleo', 3.20, 'Sal', 1.80, 'Açucar', 6, 'Leite', 3.4)
print('-'*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-'*40)
for pos in range(0,len(listagem)):
    if pos % 2 == 0 :
        print(f'{listagem[pos]:.<30}', end='')
    else:
      print(f'R${listagem[pos]:>7.2f}')
