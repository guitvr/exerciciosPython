# coding: utf-8

# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

n = int(input("Digite a quantidade de eleitores: "))

c1 = c2 = c3 = 0

for i in range(n):
    print(f"""
Eleitor {i+1}:
Digite 1 para o candidato 1;
       2 para o candidato 2;
    ou 3 para o candidato 3.
    """)
    voto = int(input("Seu voto: "))

    while not 1 <= voto <= 3:
        print("Voto inválido!")

        print(f"""
Eleitor {i + 1}:
Digite 1 para o candidato 1;
       2 para o candidato 2;
    ou 3 para o candidato 3.
            """)
        voto = int(input("Seu voto: "))

    if voto == 1:
        c1 += 1
    elif voto == 2:
        c2 += 2
    elif voto == 3:
        c3 += 3

total = c1 + c2 + c3

print(f"""

Candidato 1: {c1/total*100:.2f}%  ({c1} votos)
Candidato 2: {c2/total*100:.2f}%  ({c2} votos)
Candidato 3: {c3/total*100:.2f}%  ({c3} votos)
""")
