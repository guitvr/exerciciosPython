# coding: utf-8

# Faça um programa que pergunte o preço de três produtos e informe qual produto
# você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input("Digite o preço do produto 1: R$"))
p2 = float(input("Digite o preço do produto 2: R$"))
p3 = float(input("Digite o preço do produto 3: R$"))

maisBarato = "Produto "

if p1 <= p2:
    if p1 <= p3:
        maisBarato += "1"
    else:
        maisBarato += "3"
elif p2 <= p1:
    if p2 <= p3:
        maisBarato += "2"
    else:
        maisBarato += "3"

print(f"O produto mais barato é o {maisBarato}")
