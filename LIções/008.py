peso = float(input('Digite seu peso: '))
tamanho = float(input('Digite sua autura: '))

imc = tamanho * tamanho / peso

if imc < 18.5:
    print('Abaixo do peso.')

elif imc >= 18.5 and imc < 25:
    print('Peso ideal.')

elif imc >= 25 and imc < 30:
    print('Acima do peso.')

elif imc >= 30 and imc < 40:
    print('Obesidade.')

else:
    print('Obesidade mórbida.')