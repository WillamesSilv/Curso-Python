tb = 0
while True:
    tb = int(input('Quer ver a tabuada de qual número? '))
    if tb == -1:
        break

    for c in range(0, 11):
        print(f'{tb} x {c} = {tb * c}')

print('Fim')
