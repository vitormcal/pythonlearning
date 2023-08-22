n = int(input('Digite um número inteiro para saber se ele é primo ou não: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\33[32m', end=' ')
        total += 1

    else:
        print('\33[31m', end=' ')
    print('{} '.format(c), end=' ')
print('''

\33[1;32mO número {} foi divisível {} vezes'''.format(n, total))
if total == 2:
    print('O número digitado É PRIMO!')
else:
    print('O número digitado NÃO É PRIMO!')


