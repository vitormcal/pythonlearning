r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3+r1 > r2:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')