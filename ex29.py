velocidade = float(input('Digite a velocidade: '))
multa = (velocidade - 80) *7
if velocidade >80:
    print('Você foi multado! O valor da multa é de R${:.2f}'.format(multa))
else:
    print('Você passou dentro dos limites da via!')
