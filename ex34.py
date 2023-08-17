salario = float(input('Digite o valor de seu salário para saber o aumento: R$ '))
salario15 = salario + (salario * 0.15)
salario10 = salario + (salario * 0.10)
if salario > 1250.00:
    print('O novo salário, com aumento de 10%, é de R$ {:.2f}'.format(salario10))
else:
    print('O novo salário, com aumento de 15%, é de R$ {:.2f}'.format(salario15))
