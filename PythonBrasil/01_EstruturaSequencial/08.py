# coding: utf-8

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valorPorHora = float(input("Digite o quanto você ganha por hora trabalhada: R$"))
horasTrabalhadas = float(input("Digite quantas horas você trabalhou: "))

salario = valorPorHora * horasTrabalhadas

print(f"Você receberá R${salario:.2f}")
