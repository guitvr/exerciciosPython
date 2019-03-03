# coding: utf-8

# Faça um Programa para leitura de três notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e presentar:
#   A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#   A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#   A mensagem "Aprovado com Distinção", se a média for igual a 10.

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

media = (n1 + n2 + n3) / 3

print(f"\nMédia: {media:.1f}\n")

if media >= 7.0:
    if media == 10:
        print("Aprovado com Distinção")
    else:
        print("Aprovado")
elif media < 7.0:
    print("Reprovado")
