from time import sleep
n = input('\033[7;30mDigite algo:\033[m ')
print('\033[1;30;42mPROCESSANDO...\033[m')
sleep(3)
print('\033[1mO tipo primitvo desse valor é\033[m', type(n))
print('\033[1mSó tem espaços?\033[m', n.isspace())
print('\033[1mÉ um número?\033[m', n.isnumeric())
print('\033[1mÉ um alfabeto?\033[m', n.isalpha())
print('\033[1mÉ um alfanumerico?\033[m', n.isalnum())
print('\033[1mEstá em maiuscula?\033[m', n.isupper())
print('\033[1mEstá em minuscula?\033[m', n.islower())
print('\033[1mEstá capitalizado?\033[m', n.istitle())

