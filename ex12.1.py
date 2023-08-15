preçoantigo = float(input('Digite o preço de um produto para saber o seu valor com 5% de desconto: R$'))
novopreço = preçoantigo - (preçoantigo * 5 / 100)
print("O novo preço com 5% de desconto é: R${:.2f}".format(novopreço))