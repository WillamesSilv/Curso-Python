l = float(input('\033[1;35mDigite a largura da parede:\033[m '))
a = float(input('\033[1;34mDigite a altura da parede:\033[m '))
area = l*a
tinta = area/2
print('Sua parede tem dimensão de \033[4;33m{}x{}\033[m e sua área é de \033[4;36m{:.2f}m²\033[m.'.format(l, a, area))
print('Para pintar essa parede, você precisará de \033[4;31m{:.3f}L\033[m de tinta.'.format(tinta))

