salario=float(input('Digite o salário atual: '))
reajuste1 = salario * 1.35
reajuste2 = salario * 1.15
if salario <= 300: print('O salário foi aumentado para',reajuste1)
else: print('O salário foi aumentado para',reajuste2)