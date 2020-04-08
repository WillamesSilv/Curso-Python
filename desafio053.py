'''frase = str(input('Digite uma frase: ')).upper().strip().replace(' ', '')
print('A frase {} no inverso é {}.'.format(frase, frase[::-1]))
if frase == frase[::-1]:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase NÃO É UM PALÍNDROMO!')'''#minha resolução, abaixo a do prof. Guanabara usando for

frase = str(input('Digite uma frase e descubra se ela é um PALÍNDROMO: ')).strip().upper()
separada = frase.split()
juntas = ''.join(separada)
inverso = ''
for letra in range(len(juntas) -1, -1, -1):
    inverso += juntas[letra]
print('A frase {} no inverso é {}'.format(juntas, inverso))
if juntas == inverso:
     print('Temos um PALÍNDROMO!')
else:
     print('Não temos um PALÍNDROMO')