# coding: utf-8

# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
# pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#   a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
#       pedir os demais valores, sendo encerrado;
#   b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#   c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#   d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

print("Para uma equação do segundo grau na forma ax² + bx + c, informe os valores de:")
a = float(input("a: "))
if a == 0:
    print("a = 0\nEquação não é do segundo grau")
else:
    b = float(input("b: "))
    c = float(input("c: "))
    delta = (b**2) - (4*a*c)

    if delta < 0:
        print("Delta negativo. A equação não possui raízes reais.")
    elif delta == 0:
        x = (-b)/(2*a)
        print(f"x = {x}")
    elif delta > 0:
        x1 = (-b + (delta**(1/2)))/(2*a)
        x2 = (-b - (delta**(1/2)))/(2*a)
        print(f"x1 = {x1}\nx2 = {x2}")
