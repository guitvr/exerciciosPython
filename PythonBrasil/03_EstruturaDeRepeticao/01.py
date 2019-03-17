# coding: utf-8

# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso
# o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("Digite uma nota (de 0 à 10): "))

while not (0 <= nota <= 10):
    nota = float(input("Nota inválida.\nDigite uma nota (de 0 à 10): "))
