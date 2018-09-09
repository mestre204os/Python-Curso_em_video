idade = int(input('Quantos anos você tem?'))
falta = 18 - idade
sobra = idade - 18
if idade < 18:
    print('Faltam {} anos para você se alistar para o exército.'.format(falta))

elif idade > 18:
    print('Se você não se alistou, já devia ter se alistado a {} anos.'.format(sobra))

else:
    print('Está na hora de se alistar.')