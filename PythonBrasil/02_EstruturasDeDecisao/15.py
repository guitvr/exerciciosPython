# coding: utf-8

# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar
# se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
# se o mesmo é: equilátero, isósceles ou escaleno.

print("Digite 3 valores e direi se é possível fazer um triângulo e de qual tipo")
n1 = float(input("Valor 1: "))
n2 = float(input("Valor 2: "))
n3 = float(input("Valor 3: "))

isTriangle = False

if (n1 + n2) > n3 and (n1 + n3) > n2 and (n2 + n3) > n1:
    isTriangle = True

if isTriangle:
    if n1 == n2 == n3:
        print("Estas três medidas formam um triângulo equilátero.")
    elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
        print("Estas três medidas formam um triângulo isósceles.")
    elif n1 != n2 != n3:
        print("Estas três medidas formam um triângulo escaleno.")
else:
    print("Estas três medidas não formam um triagulo.")
