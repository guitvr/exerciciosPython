# coding: utf-8

# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

s = True if int(input("Digite seu sexo [0] Masculino / [1] Feminino:  ")) else False
h = float(input("Digite sua altura: "))

if s:  # Se for mulher
    p = (62.1*h) - 44.7
else:
    p = (72.7*h) - 58

print(f"Seu peso ideal é de {p:.2f} Kg")
