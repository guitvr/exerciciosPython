# coding: utf-8

# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
#
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral
# do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

cardapio = {100: {"preco": 1.2, "espec": "Cachorro Quente"},
            101: {"preco": 1.3, "espec": "Bauru Simples"},
            102: {"preco": 1.5, "espec": "Bauru com ovo"},
            103: {"preco": 1.2, "espec": "Hambúrguer"},
            104: {"preco": 1.3, "espec": "Cheeseburguer"},
            105: {"preco": 1, "espec": "Refrigerante"}}

print("Cardápio:\nEspecificação   Código  Preço")
for produto in cardapio:
    print(cardapio[produto]["espec"].ljust(15, " "),
          str(produto).ljust(7, " "),
          "R$", format(cardapio[produto]["preco"], ".2f"))

total = 0
pedido = []

while True:
    print()
    opcao = int(input("Digite sua opção: "))
    qnt = int(input("Digite a quantidade: "))

    item = [opcao, qnt]
    pedido.append(item)

    sair = True if str(input("Deseja finalizar o pedido? [s - sim, n - não]: ")).lower() == "s" else False
    if sair:
        break

print("""

Pedido:
""")
for item in pedido:
    itemPreco = item[1]*cardapio[item[0]]['preco']
    total += itemPreco
    print(f"{item[1]} x {cardapio[item[0]]['espec']}".ljust(25, " "), f" = R$ {itemPreco:.2f}")

print(f"\nTotal: R$ {total:.2f}")
