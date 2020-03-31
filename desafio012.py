pr = float(input('\033[1;32;40mQual o preço do produto?\033[m R$'))
des = pr - (pr * 5 / 100)
print('\033[1;31mO preço do produto com 5% de desconto é R${:.2f}'.format(des))
