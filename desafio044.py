print('{:=^40}'.format(' LOJAS WILLAMES '))# O ACENTO (^) QUER DIZER CENTRALIZADO
preço = float(input('Qual é o preço das compras? R$'))
vista = preço - (preço * 10 / 100)
cartão = preço - (preço * 5 / 100)
juros = preço + (preço * 20 / 100)
pagamento = int(input('''Escolha a forma de pagamento
[1] - A VISTA
[2] - A VISTA NO CARTÃO
[3] - EM ATÉ 2X NO CARTÃO
[4] - EM ATÉ 3X OU MAIS NO CARTÃO
 Qual a sua opção? '''))
if pagamento == 1:
    print('A VISTA recebe 10% de desconto, valor a pagar é R${:.2f}.'.format(vista))
elif pagamento == 2:
    print('A VISTA NO CARTÃO recebe 5% de desconto, valor a pagar é R${:.2f}.'.format(cartão))
elif pagamento == 3:
    print('PAGAMENTO EM 2X NO CARTÃO, valor a pagar é R${:.2f} em 2x de R${:.2f}.'.format(preço, preço / 2))
elif pagamento == 4:
    vezes = int(input('Em quantas vezes quer pagar? '))
    print('Pagamento em {} vezes no cartão, valor da parcela R${:.2f}.'.format(vezes, juros / vezes))

