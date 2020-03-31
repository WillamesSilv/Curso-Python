r = float(input('\033[1;31;46mQuanto dinheiro você tem em sua carteira?\033[m R$'))
d = r/3.27
print('Convertendo o valor em sua carteira de \033[1;34mR${:.2f}\033[m, você tem \033[1;36mUS${:.2f}\033[m.'.format(r, d))
