# coding: utf-8

# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

c = float(input("Digite a temperatura em graus Celsius: "))
f = (c * 9 / 5) + 32

print(f"{c}°C = {f:.2f}°F")
