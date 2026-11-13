for c in range (5):
    compra = float(input('Qual o valor da venda?'))
    if compra >= 200:
        desconto = compra * 0.10
        total = compra - desconto
        print(f'Valor da compra R${compra}\nValor do desconto: R${desconto}\nO total é R${total}')
    else:
        print('Sem desconto')

