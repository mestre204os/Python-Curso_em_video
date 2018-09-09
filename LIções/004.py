nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi sua segunda nota? '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('Você foi reprovado.')

elif media >= 5.0 and media < 6.9:
    print('Está de recuperação.')

else:
    print('Aprovado.')