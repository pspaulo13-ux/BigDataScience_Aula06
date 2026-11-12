ingresso = float(input('Qual o valor do ingresso?'))

print('''
Escolha uma das opções disponíveis:

[1] Inteira (Sem desconto)
[2] Meia entrada (50% de desconto)
[3] Promoção (30% de desconto)

''')

opcao = int(input('Informe a opção escolhida: '))
desconto = 0

match opcao:
    case 1:
        print('-Inteira-')
        desconto = 0         
    case 2:
        print('-Meia entrada-')
        desconto = ingresso * 0.50
    case 3:
        print('-Promoção-')
        desconto = ingresso *0.30
    case _:
        print('Opção inválida')
        exit()

valor_final = ingresso - desconto

print(f'O valor do seu ingresso é: R${ingresso}\nDesconto: R${desconto}\nValor final: R${valor_final}')
    



