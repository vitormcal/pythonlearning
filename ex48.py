soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('Foram encontrados {} números'.format(cont))
print('A soma dos valores solicitados é {}'.format(soma))
