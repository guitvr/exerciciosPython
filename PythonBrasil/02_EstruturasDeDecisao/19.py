# coding: utf-8

# Faça um Programa que leia um número inteiro menor que 1000 e
# imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = int(input("Digite um número (menor que 1000): "))

if num >= 1000:
    print("Número inválido.")

else:
    centenas = num // 100
    dezenas = (num % 100) // 10
    unidades = num % 10

    msg = ""

    if centenas > 0:
        msg += f"{centenas} centena" if centenas == 1 else f"{centenas} centenas"

        if dezenas > 0 and unidades > 0:
            msg += ", "
        elif dezenas == 0 and unidades > 0 or dezenas > 0 and unidades == 0:
            msg += " e "

    if dezenas > 0:

        msg += f"{dezenas} dezena" if dezenas == 1 else f"{dezenas} dezenas"

        if unidades > 0:
            msg += " e "

    if unidades > 0:
        msg += f"{unidades} unidade" if unidades == 1 else f"{unidades} unidades"

    print(msg)
