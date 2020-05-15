tb = 0
while True:
    tb = int(input('Quer ver a tabuada de qual número? '))
    for c in range (0, 11):
        print(f'{tb} x {c} = {tb * c}')
    if tb == -1:
        break
print('Fim')
