ano = int(input('Digite um ano: '))
resultado = ano % 4
if resultado == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('Sim, o ano {} é bissexto'.format(ano))
else:
    print(('Não, o ano {} não é bissexto'.format(ano)))