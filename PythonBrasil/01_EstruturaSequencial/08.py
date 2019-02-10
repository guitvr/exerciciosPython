# coding: utf-8

valorPorHora = float(input("Digite o quanto você ganha por hora trabalhada: R$"))
horasTrabalhadas = float(input("Digite quantas horas você trabalhou: "))

salario = valorPorHora * horasTrabalhadas

print(f"Você receberá R${salario:.2f}")
