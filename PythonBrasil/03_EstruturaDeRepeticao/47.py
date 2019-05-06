# coding: utf-8

# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
# A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as
# notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição
# acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são
# informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
#
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7
#
# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04


atleta = str(input("Atleta: "))
notas = []
soma = 0

for i in range(7):
    n = float(input(f"Nota: "))
    notas.append(n)
    soma += n
soma = soma - max(notas) - min(notas)
media = soma / (len(notas) - 2)

print(f"\n\nAtleta: {atleta}\n")

for n in notas:
    print(f"Nota: {n}")

print(f"""
Resultado final:
Atleta: {atleta}
Melhor nota: {max(notas)}
Pior nota: {min(notas)}
Média: {media:.2f}
""")
