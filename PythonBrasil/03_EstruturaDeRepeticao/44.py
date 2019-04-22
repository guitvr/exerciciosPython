# coding: utf-8

# Em uma eleição presidencial existem quatro candidatos. Os votos são informados
# por meio de código. Os códigos utilizados são:
#
# 1, 2, 3, 4 - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

candidatos = {
    1: {'nome': 'José', 'votos': 0},
    2: {'nome': 'João', 'votos': 0},
    3: {'nome': 'Cláudio', 'votos': 0},
    4: {'nome': 'Caio', 'votos': 0},
    5: {'nome': 'Votos nulos', 'votos': 0},
    6: {'nome': 'Votos em branco', 'votos': 0},
}
total = 0

print("Candidatos:")
for i in candidatos:
    print(i, '-', candidatos[i]['nome'])

while True:
    voto = int(input("\nDigite seu voto: "))
    if voto == 0:
        break
    elif not 0 <= voto <= 6:
        print("Opção inválida, voto não registrado. Tente novamente.")
        continue
    print('teste')
    candidatos[voto]['votos'] += 1
    total += 1

print(f"""

Totais:
{total} votos foram computados""")

for i in candidatos:
    print(candidatos[i]['nome'].ljust(16), '=', candidatos[i]['votos'], 'votos')

print(f"""
{round(candidatos[5]['votos']/total*100, 2)}% de votos nulos
{round(candidatos[6]['votos']/total*100, 2)}% de votos em branco
""")
