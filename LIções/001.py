casa = float(input('Qual é o valor da casa? '))
salario = float(input('Quanto você recebe por mês? '))
tempo = int(input('Em quanto anos você pretende pagar? '))

valor_mensal = casa / tempo

salario_minimo = salario * 30 / 100

if valor_mensal > salario_minimo:
    print('O contrato não pode ser firmado.')

else:
    print("{} é o valor a ser pago por mês.".format(valor_mensal))