largura = float(input('Qual a largurada parede em metros? '))
altura = float(input('Qual a altura da parede em metros? '))
area = altura * largura
tinta = area / 2
print ('A area da parede é de {}m'.format(area))
print ('Para pintar a parede será necessário {} litros de tinta'.format(tinta))