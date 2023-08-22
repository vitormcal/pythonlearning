valorcasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
tempo = int(input('Em quantos anos pretende pagar? '))
meses = tempo * 12
parcela = valorcasa / meses
print('Para pagar uma casa de R${:.2f} em {} anos a pretação será de R${:.2f}'.format(valorcasa, tempo, parcela))
if  parcela >= salario * 0.30:
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo APROVADO!')