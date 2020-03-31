import math
co = float(input('\033[35mQual o comprimento em metros do cateto oposto? '))
ca = float(input('\033[31mQual o comprimento em metros do cateto adjacente? '))
hi = math.hypot(co, ca)
print('\033[34mConforme comprimento \033[1;34m{}m \033[0;34mdo cateto oposto e comprimento \033[1;34m{}m \033[0;34mdo cateto adjacente.'.format(co, ca))
print('A hipotenusa mede \033[1;31m{:.2f}m'.format(hi))















