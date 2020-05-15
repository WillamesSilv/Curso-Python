tb = 0
while True:
    tb = int(input('Quer ver a tabuada de qual número? '))
    print('\033[33m='*35)
    if tb < 0:
        break
    for c in range(0, 11):
        print(f'\033[34m{tb} x {c} = {tb * c}\033[m')
    print('\033[33m=\033[m'*35)
print('\033[31mPROGRAMA DE TABUADA ENCERRADO.')
