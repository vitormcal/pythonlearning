r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3+r1 > r2:
    print('As retas podem formam um triângulo!')
    if r1 == r2 and r1 == r3:
        print('As retas formam um triângulo Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('As retas formam um triângulo Isósceles')
    elif r1 + r2 > r3 and r2 + r3 > r1 and r3+r1 > r2:
        print('As retas formam um triângulo Escaleno')
else:
    print('A retas não podem formar um triângulo')
