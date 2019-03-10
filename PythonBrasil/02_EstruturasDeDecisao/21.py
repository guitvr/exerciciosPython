# coding: utf-8

# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor
# do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis
# serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#   Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece
#       duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#   Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
#       três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valorSaque = int(input("Digite o valor do saque (entre R$10 e R$600): R$"))

if 10 <= valorSaque <= 600:
    notas100 = valorSaque // 100
    notas50 = (valorSaque % 100) // 50
    notas10 = (valorSaque % 100 % 50) // 10
    notas5 = (valorSaque % 100 % 50 % 10) // 5
    notas1 = valorSaque % 100 % 50 % 10 % 5

    print(f"{notas100} nota(s) de R$100")
    print(f"{notas50} nota(s) de R$50")
    print(f"{notas10} nota(s) de R$10")
    print(f"{notas5} nota(s) de R$5")
    print(f"{notas1} nota(s) de R$1")

else:
    print("Valor inválido.\nValor mínimo: R$10\nValor máximo: R$600")
