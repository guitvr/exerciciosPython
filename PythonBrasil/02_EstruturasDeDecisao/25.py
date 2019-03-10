# coding: utf-8

# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#   "Telefonou para a vítima?"
#   "Esteve no local do crime?"
#   "Mora perto da vítima?"
#   "Devia para a vítima?"
#   "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


print("""
---------  Robot Holmes  ---------
O detetive eletrônico mais esperto
   e inteligente da internet

Com apenas cinco perguntas sobre o
 crime descobrirei qual foi sua 
    participação no crime.
----------------------------------


Responda com 1 para sim e 0 para não:
""")

respostasPositvas = 0

respostasPositvas += 1 if int(input("Telefonou para a vítima? ")) == 1 else 0
respostasPositvas += 1 if int(input("Esteve no local do crime? ")) == 1 else 0
respostasPositvas += 1 if int(input("Mora perto da vítima? ")) == 1 else 0
respostasPositvas += 1 if int(input("Devia para a vítima? ")) == 1 else 0
respostasPositvas += 1 if int(input("Já trabalhou com a vítima? ")) == 1 else 0

if respostasPositvas == 2:
    participacao = "um suspeito"
elif 3 <= respostasPositvas <= 4:
    participacao = "um cúmplice"
elif respostasPositvas == 5:
    participacao = "o assassino"
else:
    participacao = "inocente"

print(f"\n\nVocê é {participacao}.")
