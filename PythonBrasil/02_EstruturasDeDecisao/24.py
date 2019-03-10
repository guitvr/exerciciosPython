# coding: utf-8

# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#   par ou ímpar;
#   positivo ou negativo;
#   inteiro ou decimal.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
op = int(input("""
Digite [1] para soma 
       [2] para subtração
       [3] para multiplicação
       [4] para divisão

Sua escolha: """))

if 1 <= op <= 4:
    if op == 1:
        result = num1 + num2
        print(f"\n{num1} + {num2} = {result}")
    elif op == 2:
        result = num1 - num2
        print(f"\n{num1} - {num2} = {result}")
    elif op == 3:
        result = num1 * num2
        print(f"\n{num1} * {num2} = {result}")
    elif op == 4:
        result = num1 / num2
        print(f"\n{num1} / {num2} = {result}")

    posOuNeg = "é positivo" if result > 0 else "é negativo"
    intOuDec = "é inteiro" if round(result) == result else "é decimal"
    if intOuDec == "é inteiro":
        parOuImpar = "é par" if result % 2 == 0 else "é ímpar"
    else:
        parOuImpar = "não é par e não é ímpar pois nao pertence ao conjunto dos números inteiros"

    print(f"\n{result} é um número que {parOuImpar}, {posOuNeg} e {intOuDec}.")

else:
    print("Opção inválida!!")
