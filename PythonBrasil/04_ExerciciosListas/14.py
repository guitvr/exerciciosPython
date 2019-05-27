# coding: utf-8

# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da
# pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "Já trabalhou com a vítima? "
]

classificacao = [
    "Suspeito",
    "Cúmplice",
    "Assassino",
    "Inocente",
]

print("Por favor, responda as perguntas com S (sim) ou N (não)")

respostasVerdadeiras = 0

for p in perguntas:
    respostasVerdadeiras = respostasVerdadeiras + 1 if str(input(p)).lower() == 's' else respostasVerdadeiras + 0

if respostasVerdadeiras == 2:
    print(f"Você é {classificacao[0]}")
elif 2 < respostasVerdadeiras <= 4:
    print(f"Você é {classificacao[1]}")
elif respostasVerdadeiras == 5:
    print(f"Você é {classificacao[2]}")
else:
    print(f"Você é {classificacao[3]}")
