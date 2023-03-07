num1=float(input('Digite um número: '))
num2=float(input('Digite um número: '))
print('Opção 1 - SOMA')
print('Opção 2 - SUBTRAÇÃO')
opcao=int(input('Digite o número da opção que deseja escolher:'))
r1 = num1 + num2
r2 = num1 - num2
if opcao == 1: print('O resultado da soma é: ',r1)
else: print('O resultado da subtração é: ',r2)