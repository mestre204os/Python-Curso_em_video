produto = float(input('Qual o preço do produto? '))

modo_pagamento = input('Como você deseja pagar? \n Para pagar a vista em dinheiro, Digite 1. \n Para pagar a vista com o cartão, digite 2. \n para pagar parcelado em duas vezes, digite 3. \n Para pagar parcelado em três ou mais vezes, digite 4. ')

if modo_pagamento == '1':
    pagar = produto - (10 / 100 * produto)
    print('O preço com desconto fica {}'.format(pagar))

elif modo_pagamento == '2':
    pagar = produto - (5 / 100 * produto)
    print('O preço com desconto fica {}'.format(pagar))

elif modo_pagamento == '3':
    print('Não te desconto. O preço é {}'.format(produto))

elif modo_pagamento == '4':
    parcela = int(input('Em quantas parcelas você pretende pagar?'))
    pagar = (produto + (20 / 100 * produto)) / parcela
    print('Você vai pagar {} em {} vezes com 20% de juros. A parcela fica {}'.format(produto, parcela, pagar))