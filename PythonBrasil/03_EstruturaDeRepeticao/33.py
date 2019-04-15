# coding: utf-8

# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa
# que leia um conjunto indeterminado de temperaturas, e informe ao final a menor
# e a maior temperaturas informadas, bem como a média das temperaturas.

soma = c = 0
while True:
    t = float(input("\nDigite uma temperatura (em °C): "))
    soma += t
    c += 1

    if c == 1:
        maior = menor = t
    else:
        if t > maior:
            maior = t
        if t < menor:
            menor = t

    op = int(input("Deseja informar mais dados? 1-Sim/ 0-Não: "))

    if op == 0:
        break

print(f"""
Maior temperatura: {maior}°C
Menor temperatura: {menor}°C
Média das temperaturas: {soma/c:.2f}°C
""")
