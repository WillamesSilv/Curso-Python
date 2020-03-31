d = int(input('\033[1;31mQuantos dias alugados? '))
km = float(input('\033[1;32mQuantos km rodado? '))
print('\033[33mO valor total a pagar é R${:.2f}'.format((60.0*d) + km*0.15))
