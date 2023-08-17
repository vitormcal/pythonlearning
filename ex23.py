numero = int(input('Digite um número inteiro de 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o número {} ...'.format(numero))
print('A unidade de {} é: {}'.format(numero, u))
print('A dezena de {} é: {}'.format(numero, d))
print('A centena de {} é: {}'.format(numero, c))
print('A milhar de {} é: {}'.format(numero, m))