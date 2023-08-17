distancia = float(input('Qual a distancia da sua viagem? '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(('A sua passagem será de R${:.2f}'.format(preco)))