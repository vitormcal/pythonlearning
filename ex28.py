from random import randint

numero = int(input('Digite um número de 0 a 5: '))
computador = randint(0, 5)
if numero == computador:
    print('Você acertou, o número é {}'.format(computador))
else:
    print('Você errou! O número que pensei foi: {}'.format(computador))