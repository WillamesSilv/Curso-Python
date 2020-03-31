salário = float(input('\033[33mQual é o salário do funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('\033[1;34mO salário do funcionário que é de R${:.2f}, com aumento de 15%, passará a ser de R${:.2f}'.format(salário, novo))
