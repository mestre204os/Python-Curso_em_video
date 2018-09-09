idade = int(input('Quantos anos você tem?'))
'''mirim = idade <= 9
infantil = idade > 9 and idade <= 14
junior = idade > 14 and idade <= 19
senior = idade > 19 and idade <= 20'''
if idade == idade <= 9:
    print('Você é um nadador mirim.')

elif idade == idade > 9 and idade <= 14:
    print('Você é um nadador infantil.')

elif idade == idade > 14 and idade <= 19:
    print('Você é um nadador junior.')

elif idade == idade > 19 and idade <= 20:
    print('Você é um nadador sênior.')

else:
    print('Você é um nadador master.')