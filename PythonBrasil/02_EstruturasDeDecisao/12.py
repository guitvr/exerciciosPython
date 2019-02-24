# coding: utf-8

# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
# Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
# menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
#   Salário Bruto até 900 (inclusive) - isento
#   Salário Bruto até 1500 (inclusive) - desconto de 5%
#   Salário Bruto até 2500 (inclusive) - desconto de 10%
#   Salário Bruto acima de 2500 - desconto de 20%

valorHora = float(input("Digite o valor da hora trabalhada: R$"))
qtdHora = float(input("Digite a quantidade de horas trabalhadas: "))

bruto = valorHora * qtdHora

# Imposto de Renda
if bruto <= 900:
    IR = 0
elif 900 < bruto <= 1500:
    IR = 5
elif 1500 < bruto <= 2500:
    IR = 10
elif bruto < 2500:
    IR = 20
valorIR = bruto * (IR / 100)

# INSS:
INSS = 10
valorINSS = bruto * (INSS / 100)
# FGTS:
FGTS = 11
valorFGTS = bruto * (FGTS / 100)

totalDescontos = valorINSS + valorIR
liquido = bruto - totalDescontos

print()
print(f"Salário bruto ({valorHora} * {qtdHora})".ljust(30), f":R${bruto:.2f}")
print(f"( - ) IR ({IR}%)".ljust(30), f":R${valorIR:.2f}")
print(f"( - ) INSS ({INSS}%)".ljust(30), f":R${valorINSS:.2f}")
print(f"FGTS ({FGTS}%)".ljust(30), f":R${valorFGTS:.2f}")
print(f"Total de descontos".ljust(30), f":R${totalDescontos:.2f}")
print(f"Salário líquido".ljust(30), f":R${liquido:.2f}")
