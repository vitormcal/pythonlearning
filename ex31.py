distancia = float(input('Qual a distancia da viagem? '))
preco1 = distancia / 2
preco2 = distancia / 2 - (distancia * 0.05)
if distancia <= 200:
    print('O valor da viagem é de R$ {:.2f}'.format(preco1))
else:
    print('O valor da viagem é de R$ {:.2f}'.format((preco2)))
