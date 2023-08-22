A1 = float(input('Digite a nota A1: '))
A2 = float(input('Digite a nota A2: '))
media = (A1 + A2) / 2
print('Quem tirou {:.1f} e {:.1f} tem a média {:.1f}!'.format(A1, A2, media))
if media < 5.0:
    print('O aluno foi REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno foi APROVADO!')