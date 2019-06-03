# coding: utf-8

# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será
# determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco
# distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
# O programa deve ser encerrado quando não for informado o nome do atleta.
# A saída do programa deve ser conforme o exemplo abaixo:
#
# Atleta: Rodrigo Curvêllo
#
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
#
# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

while True:
    nome = str(input("Atleta: ")).strip()

    if nome == '':
        break

    print()

    saltos = [0, 0, 0, 0, 0]

    saltos[0] = float(input("Primeiro salto: "))
    saltos[1] = float(input("Segundo salto: "))
    saltos[2] = float(input("Terceiro salto: "))
    saltos[3] = float(input("Quarto salto: "))
    saltos[4] = float(input("Quinto salto: "))

    print("\nResultado final:")
    print(f"Atleta: {nome}")
    print("Saltos: ", end='')

    for i in range(5):
        if i == 4:
            print(f"{saltos[i]}")
        else:
            print(f"{saltos[i]} - ", end='')

    print(f"Média dos saltos: {sum(saltos)/len(saltos):.1f} m")

    print()
