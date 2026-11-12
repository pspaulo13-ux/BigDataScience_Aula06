valor = float(input('Valor da venda: '))

print('''
[1] - PIX (12% de desconto)
[2] - Débito (8% de desconto)
[3] - Crédito (5% de desconto)
[4] - Dinheiro (15% de desconto)
''')
#operacao = True, essa é para dizer que as opcões só são válidas se estiverem dentro das operações abaixo
desconto = 0
opcao = int(input('Informe a opção escolhida: '))

match opcao:
    case 1:
        print('---PIX---')
        desconto = valor * 0.12
        #Essa é uma das formas que daria para ser feito, mas teria que aplicar essa mesma estrutura em todos os outros cases.
        #valor_final = valor - desconto
        #print(f'Sua compra ficou no valor de R${valor}\nSeu desconto foi de R${desconto}\nO valor final da sua compra é R${valor_final}')

    case 2:
        print('---Débito---') 
        desconto = valor * 0.08

    case 3:
        print('---Crédito---')
        desconto = valor * 0.05

    case 4:
        print('---Dinheiro---')
        desconto = valor * 0.15

    case _:
        print('Opção inválida')

#Agora temos outras opções:
if opcao in [1, 2, 3, 4]: # Essa diz que o código só pode ir a diante se o valor digitado está entre essas opções.
#if operacao == True, ess é para válida a operação se ela está dentro das opçoes que foi dita la em cima como true
#if desconto != 0: #O sinal de ! significa diferente
    valor_final = valor - desconto
    print(f'\nPreço: R${valor}\nDesconto: R${desconto}\nTotal a pagar: R${valor_final}')

else:
    print("Por favor escolha uma das opções acima")



