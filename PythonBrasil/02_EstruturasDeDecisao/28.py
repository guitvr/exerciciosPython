# coding: utf-8

# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de
# carne da promoção, porém não há limites para a quantidade de carne por cliente. Se
# compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre
# o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada
# pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade
# de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

tipoCarne = str(input("Digite o tipo da carne ( F - Filé Duplo, A - Alcatra, P - Picanha ): ")).lower()
qntCarne = float(input("Digite a quantidade de carne (em Kg): "))
pagamento = int(input("Forma de pagamento (1 - Cartão Tabajara, 2 - Crédito, 3 - Débito, 4 - Dinheiro): "))

carne = ''
preco = 0
formaPagamento = ''

if pagamento == 1:
    formaPagamento = 'Cartão Tabajara'
elif pagamento == 2:
    formaPagamento = 'Crédito'
elif pagamento == 3:
    formaPagamento = 'Débito'
elif pagamento == 4:
    formaPagamento = 'Dinheiro'

if tipoCarne == 'f':
    carne = 'Filé Duplo'
    preco = 4.9 * qntCarne if qntCarne <= 5.0 else 5.8 * qntCarne

elif tipoCarne == 'a':
    carne = 'Alcatra'
    preco = 5.9 * qntCarne if qntCarne <= 5.0 else 6.8 * qntCarne

elif tipoCarne == 'p':
    carne = 'Picanha'
    preco = 6.9 * qntCarne if qntCarne <= 5.0 else 7.8 * qntCarne

desconto = preco * 0.1 if pagamento == 1 else 0
total = preco - desconto

print(f"\ncarne: {carne}")
print(f"quantidade: {qntCarne}Kg")
print(f"preço: R${preco}")

print(f"""
-------------- CUPOM FISCAL --------------

Produto        Quantidade        Preço

{carne.ljust(15)}{(str(qntCarne)+' Kg').ljust(18)}R$ {preco:.2f}

Tipo de pagamento: {formaPagamento}

Desconto: R$ {desconto:.2f}
Total:    R$ {total:.2f}
""")
