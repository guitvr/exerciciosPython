# coding: utf-8

# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

n = int(input("Digite a quantidade de números a ser digitada: "))

soma = 0

for i in range(n):
    num = int(input(f"n{i+1}: "))
    while not 0 <= num <= 1000:
        print("Digite apenas números entre 0 e 1000")
        num = int(input(f"n{i + 1}: "))

    if i == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    soma += num

print(f"""
Dos números digitados:
o maior é {maior}
o menor é {menor}
a soma dos números digitados é {soma}""")
