# coding: utf-8

# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar
# ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de
# acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma
# pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
#   Maior e Menor Acerto;
#   Total de Alunos que utilizaram o sistema;
#   A Média das Notas da Turma.
#   Gabarito da Prova:
#       01 - A
#       02 - B
#       03 - C
#       04 - D
#       05 - E
#       06 - E
#       07 - D
#       08 - C
#       09 - B
#       10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o
# professor digite o gabarito da prova antes dos alunos usarem o programa.

gabarito = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'E',
    7: 'D',
    8: 'C',
    9: 'B',
    10: 'A'
}

print("Professor, esse é o gabarito padrão:")
print("Questão | Resposta")

for q in gabarito:
    print(f"{str(q).center(7, ' ')} | {gabarito[q].center(8)}")
alterar = True if str(input('Deseja alterar? [s/n]: ')).lower() == 's' else False

if alterar:
    print()
    gabarito.clear()
    q = int(input("Digite quantas questões tem a prova: "))
    for i in range(1, q+1):
        r = str(input(f"Digite a resposta da questão {i}: ")).upper()
        gabarito[i] = r
    print("\nGabarito alterado\n")

print(gabarito)

peso = float(input("Quanto vale a prova? "))

print(f"\nOk, a prova vale {peso} e cada questão vale {peso/len(gabarito)}\n\n")

provaAlunos = {}

print("Aluno,\nVerifique aqui seu resultado da prova\n")

while True:

    aluno = input("Digite seu número: ")

    nota = 0
    provaAlunos[aluno] = {'acertos': 0}

    # Coleta das respostas do aluno
    for i in range(len(gabarito)):
        respostaAluno = str(input(f"Digite a sua resposta para a questão {i+1}: ")).upper()
        provaAlunos[aluno][i+1] = [respostaAluno]

        # Compara a resposta do aluno com o gabarito
        acertou = True if provaAlunos[aluno][i+1][0] == gabarito[i+1] else False

        if acertou:
            provaAlunos[aluno]['acertos'] += 1

        provaAlunos[aluno][i+1].append(acertou)

    provaAlunos[aluno]['nota'] = provaAlunos[aluno]['acertos'] * (peso/len(gabarito))

    print(f"""
    Total de acertos: {provaAlunos[aluno]['acertos']}
    Nota: {provaAlunos[aluno]['nota']}

    """)

    op = str(input("Outro aluno vai utilizar o sistema? [s/n]: ")).lower()
    if op == 'n':
        break

alunos = []
notas = []
soma = 0
for aluno in provaAlunos:
    alunos.append(aluno)
    notas.append(provaAlunos[aluno]['acertos'])
    soma += provaAlunos[aluno]['acertos']
media = soma / len(alunos)

print(f"""
Maior acerto: {max(notas)} | Aluno: {alunos[notas.index(max(notas))]}
Menor acerto: {min(notas)} | Aluno: {alunos[notas.index(min(notas))]}
Total de alunos que utilizaram o sistema: {len(provaAlunos)}
Média das notas da turma: {media:.1f}
""")
