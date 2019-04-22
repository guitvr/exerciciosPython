# coding: utf-8

# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
# Foram obtidos os seguintes dados:
#   Código da cidade;
#   Número de veículos de passeio (em 1999);
#   Número de acidentes de trânsito com vítimas (em 1999).
# Deseja-se saber:
#   Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#   Qual a média de veículos nas cinco cidades juntas;
#   Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

totalVeiculos = 0
cont = 0
totalAcidentesMenor2000 = 0

for i in range(5):
    cod = input("Digite o código da cidade: ")
    numVeiculos = int(input("Digite o número de veículos de passeio nessa cidade (em 1999): "))
    numAcidentes = int(input("Digite o número de acidentes de trânsito com vítimas nessa cidade (em 1999): "))
    print()
    if i == 0:
        maiorAcidentes = numAcidentes
        codMaiorAcidentes = cod
        menorAcidentes = numAcidentes
        codMenorAcidentes = cod

    else:
        if numAcidentes > maiorAcidentes:
            maiorAcidentes = numAcidentes
            codMaiorAcidentes = cod
        if numAcidentes < menorAcidentes:
            menorAcidentes = numAcidentes
            codMenorAcidentes = cod

    totalVeiculos += numVeiculos
    if numVeiculos < 2000:
        cont += 1
        totalAcidentesMenor2000 += numAcidentes

print(f"""

O maior índice de acidentes está na cidade {codMaiorAcidentes} com {maiorAcidentes} acidentes registrados
O menor índice de acidentes está na cidade {codMenorAcidentes} com {menorAcidentes} acidentes registrados

A média de veículos nas cinco cidades juntas é de {totalVeiculos/5} veículos.

A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é de {totalAcidentesMenor2000/cont} acidentes.

""")
