print('{:=^40}'.format(' LOJAS MEP-LEVY '))
preço = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Digite a forma de pagamento: '))
if opção == 1:
    valor = preço - preço * 0.10
    print('Sua compra será paga à vista em dinheiro ou pix, por isso, terá 10% de desconto, portanto, o valor passa a ser de R${:.2f}.'.format(valor))
elif opção == 2:
    valor = preço - preço * 0.05
    print('Sua compra será paga á vista no cartão, por isso, terá 5% de desconto, portanto, o valor passa a ser de R${:.2f}.'.format(valor))
elif opção == 3:
    valor = preço / 2
    print('Sua compra será paga em 2x no cartão, o valor total será de R${:.2f}, ou seja, R${:.2f} por parcela.'.format(preço,valor))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    valor = (preço + preço * 0.20)
    valorp = (preço + preço * 0.20) / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas,valorp))
    print('Sua compra de R${:.2f} passará a custar R${:.2f} no final.'.format(preço, valor))
else:
    print('Opção de pagamento INVÁLIDA! Tenta novamente.')


