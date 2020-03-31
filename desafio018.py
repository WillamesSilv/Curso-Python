import math
an = float(input('Digite um ângulo desejado: '))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
tg = math.tan(math.radians(an))
print('O ângulo de {} tem SENO de {:.2f}'.format(an, se))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(an, co))
print('O ângulo de  {} tem TANGENTE de {:.2f}'.format(an, tg))
