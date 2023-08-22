ano = int(input('Digite seu ano de nascimento: '))
idade = 2023 - ano
falta = 18 - idade
passou = idade - 18
print('Quem nasceu em {} tem {} anos em 2023.'.format(ano, idade))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(falta))
elif idade > 18:
    print('Já passaram {} anos para o alistamento'.format(passou))
else:
    idade == 18
    print('Este é o ano para o alistamento')
