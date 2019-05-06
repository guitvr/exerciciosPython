# coding: utf-8

# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
# atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
# informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a
# média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não
# são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser
# conforme o exemplo abaixo:
#
# Atleta: Rodrigo Curvêllo
#
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
#
# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m
#
# Resultado final:
# Rodrigo Curvêllo: 5.9 m

while True:
    atleta = str(input("Atleta: "))

    if atleta == "" or atleta.isspace() is True:
        break

    saltos = []
    soma = 0
    for i in range(1, 6):
        s = float(input(f"{i}° salto: "))
        saltos.append(s)
        soma += s

    soma = soma - max(saltos) - min(saltos)
    media = soma / (len(saltos) - 2)

    print(f"""

Atleta: {atleta}

Primeiro Salto: {saltos[0]} m
Segundo Salto:  {saltos[1]} m
Terceiro Salto: {saltos[2]} m
Quarto Salto: {saltos[3]} m
Quinto Salto: {saltos[4]} m

Melhor salto: {max(saltos)} m
Pior salto: {min(saltos)} m
Média dos demais saltos: {media:.2f} m

Resultado final:
{atleta}: {media:.2f} m

""")

