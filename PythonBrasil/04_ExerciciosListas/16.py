# coding: utf-8

# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um
# vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um
# total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam
# salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
#
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.


# ideia: definir uma fórmula que classifique cada salário numa escala de 0 à 8
# classificando dessa forma, soma-se 1 a cada categoria para medir a quantidade
#
# Lista contIntervalos, posições indicam o intervalo do salário:
# $200 - $299 - posição 0 da lista
# $300 - $399 - posição 1 da lista
# $400 - $499 - posição 2 da lista
# $500 - $599 - posição 3 da lista
# $600 - $699 - posição 4 da lista
# $700 - $799 - posição 5 da lista
# $800 - $899 - posição 6 da lista
# $900 - $999 - posição 7 da lista
# $1000 em diante - posição 8 da lista

salarios = []

print("Digite um número negativo a qualquer momento para encerrar a entrada de dados\n")

while True:
    s = float(input("Digite o total das vendas brutas de um vendedor: $"))
    if s < 0:
        break
    salarios.append(200+(0.09*s))

contIntervalos = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for s in salarios:
    f = int((s - 200) / 100)  # fórmula que define a posição da lista a partir do salário
    pos = f if f <= 8 else 8  # ajuste da posição se a fórmula resultar em um número maior que 8

    contIntervalos[pos] += 1

print(f"""
Quantidade de vendedores que receberam um salário entre:
$200 e $299: {contIntervalos[0]}
$300 e $399: {contIntervalos[1]}
$400 e $499: {contIntervalos[2]}
$500 e $599: {contIntervalos[3]}
$600 e $699: {contIntervalos[4]}
$700 e $799: {contIntervalos[5]}
$800 e $899: {contIntervalos[6]}
$900 e $999: {contIntervalos[7]}
$1000 em diante: {contIntervalos[8]}
""")
