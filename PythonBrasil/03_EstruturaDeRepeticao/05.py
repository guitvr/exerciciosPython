# coding: utf-8

# Altere o programa anterior permitindo ao usuário informar as populações e as
# taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
op = 's'
while op == 's':

    a = int(input("População A: "))
    while a <= 0:
        print("Digite um número maior que zero!")
        a = int(input("População A: "))
    taxaA = float(input("Taxa de crescimento anual da população A (em %): ")) / 100

    print()

    b = int(input("População B: "))
    while b <= 0:
        print("Digite um número maior que zero!")
        b = int(input("População B: "))
    taxaB = float(input("Taxa de crescimento anual da população B (em %): ")) / 100

    anos = 0

    while b > a:
        a += a*taxaA
        b += b*taxaB
        anos += 1

    print(f"\nSerão necessários {anos} anos para a população A ter uma quantidade maior ou igual a População B\n")
    op = str(input("Deseja repetir o cálculo? (S / N): ")).lower()
    while op not in 'sn':
        print("Digite S para sim ou N para não!")
        op = str(input("Deseja repetir o cálculo? (S / N): ")).lower()

