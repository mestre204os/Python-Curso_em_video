print('Descubra se é possível fazer um triangulo com as retas informadas abaixo')
AB = float(input('Digite o comprimenta da priemra reta: '))
AC = float(input('Digite o comprimento da segunda reta: '))
BC = float(input('Digite o comprimento  da terceira reta: '))
if ((AB + AC) > BC) and ((AB + BC) > AC) and ((AC + BC) > AB) and AB == BC and AB == AC and BC == AB:
    print('É possivel fazer um triangulo e ele é equiláterio')
elif ((AB + AC) > BC) and ((AB + BC) > AC) and ((AC + BC) > AB) and AB != BC and AB != AC and BC != AB:
    print('É possivel fazer um triângulo e ele é escaleno')
elif ((AB + AC) > BC) and ((AB + BC) > AC) and ((AC + BC) > AB) and AB == BC and AB == AC and BC == AB:
    print('É possivel fazer um triângulo e ele é isóscesles')
else:
    print('Não é possível fazer um triangulo com essas medidas')﻿
