seg1 = float(input('Digite o primeiro segmento: '))
seg2 = float(input('Digite o segundo segmento: '))
seg3 = float(input('Digite o terceiro segmento: '))
print('Analisando os segmentos {:.2f}, {:.2f} e {:.2f}.'.format(seg1, seg2, seg3))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos podem formarem um Triângulo ', end='')
    if seg1 == seg2 == seg3:
       print('EQUILÁTERO.')
    elif seg1 != seg2 != seg3 != seg1:
       print('ESCALENO.')
    else:
       print('ISÓSCELES')
else:
    print('NÃO podem formarem um triângulo!')
