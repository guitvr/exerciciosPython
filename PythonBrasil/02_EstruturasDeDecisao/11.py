# coding: utf-8

# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram
# para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um
# colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#   salários até R$ 280,00 (incluindo) : aumento de 20%
#   salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#   salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#   salários de R$ 1500,00 em diante : aumento de 5%
#   Após o aumento ser realizado, informe na tela:
#     o salário antes do reajuste;
#     o percentual de aumento aplicado;
#     o valor do aumento;
#     o novo salário, após o aumento.

salarioAtual = float(input("Digite seu salário: R$"))

if salarioAtual <= 280:
    aumento = 20
if 280 < salarioAtual <= 700:
    aumento = 15
if 700 < salarioAtual <= 1500:
    aumento = 10
if salarioAtual > 1500:
    aumento = 5

valorAumento = salarioAtual*(aumento/100)
salarioNovo = salarioAtual + valorAumento

print(f'''
Salário antes do reajuste: R${salarioAtual:.2f}
Percentual de aumento aplicado: {aumento}%
Valor do aumento: R${valorAumento:.2f}
Novo salário: R${salarioNovo:.2f}
''')
