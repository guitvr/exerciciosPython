# coding: utf-8

# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media >= 9:
    conceito = "A"
elif 7.5 >= media > 9:
    conceito = "B"
elif 6 >= media > 7.5:
    conceito = "C"
elif 4 >= media > 6:
    conceito = "D"
elif 0 >= media > 4:
    conceito = "E"

if conceito in "ABC":
    msg = "APROVADO"
elif conceito in "DE":
    msg = "REPROVADO"

print(f"""
Nota 1:    {n1:.1f}
Nota 2:    {n2:.1f}
Média:     {media:.1f}
Conceito:  {conceito}
{msg.center(14)}""")
