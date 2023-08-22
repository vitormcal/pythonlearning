soma = 0
cont = 0
for c in range (1,7):
    n = int(input('Digite o {} valor: '.format(c)))
    if soma % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('A soma dos números pares digitados é igual a {}'.format(soma))
