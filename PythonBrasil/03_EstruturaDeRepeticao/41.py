# coding: utf-8

# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
# valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1                       0
# 3                       10
# 6                       15
# 9                       20
# 12                      25
#
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67

tabelaParcelaJuros = {1: 0, 3: 0.1, 6: 0.15, 9: 0.2, 12: 0.25}

divida = float(input("Digite o valor da dívida: R$ "))

print(f"""Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela""")

for i in tabelaParcelaJuros:
    vJuros = divida * tabelaParcelaJuros[i]
    vDivida = divida + vJuros

    strVDivida = "R$ " + str(round(vDivida, 2)).ljust(14, " ")
    strVJuros = "R$ " + str(round(vJuros, 2)).ljust(14, " ")
    strQParcelas = str(i).ljust(24, " ")
    strVParcela = "R$ " + str(round(vDivida/i, 2))

    print(strVDivida, strVJuros, strQParcelas, strVParcela)
