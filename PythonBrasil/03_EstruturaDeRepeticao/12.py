# coding: utf-8

# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

num = int(input("Digite um número: "))

print(f"\nTabuada de {num}:")

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
