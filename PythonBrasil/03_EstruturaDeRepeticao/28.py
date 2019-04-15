# coding: utf-8

# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor
# médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

qntCD = int(input("Digite a quantidade de CDs: "))
total = 0
for i in range(qntCD):
    total += float(input(f"Digite o valor do CD ({i+1}/{qntCD}): "))
print(f"""

Quantidade de CDs: {qntCD}
Valor total da coleção: R${total:.2f}
Valor médio de cada CD: R${total/qntCD:.2f}
""")
