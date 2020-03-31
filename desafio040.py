nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Considerando a nota {:.1f} e {:.1f}, a média é {:.1f}.'.format(nota1, nota2, media))
if media >= 7:
    print('Parabéns o aluno foi APROVADO!')
elif media < 5:
    print('O aluno foi REPROVADO!')
elif 7 > media >= 5:
    print('O aluno ficará de RECUPERAÇÃO!')
