ano = int(input('Digite seu ano de nascimento '))
if ano > 2005:
    ano = ano - 2005
    print('Você irá se alistar daqui {} ano(s)'.format(ano))
elif ano == 2005:
    print('Está na hora de se alistar!')
else:
    ano = 2005 - ano
    print('Já passaram {} ano(s) para se alistar'.format(ano))