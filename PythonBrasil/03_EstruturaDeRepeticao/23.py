# coding: utf-8

# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

n = int(input("Digite um número inteiro: "))

print(f"Números primos entre 1 e {n}:")
cont = 0
for num in range(1, n+1):
    div = 0
    for i in range(1, num):
        if num % i == 0:
            div += 1
        cont += 1
    if div <= 1:
        print(num)
print("Número de divisões realizadas: ", cont)
