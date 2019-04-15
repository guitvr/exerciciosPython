# coding: utf-8

# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o
# mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua
# altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
# Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais
# gordo e do mais magro, além da média das alturas e dos pesos dos clientes.

cont = pesoTotal = alturaTotal = 0

while True:
    cod = int(input("\n\nDigite o código do cliente: "))
    if cod == 0:
        break
    print(f"\nCliente {cod}:")
    altura = float(input("Digite a altura (em metros): "))
    peso = float(input("Digite o peso (em Kilogramas): "))

    cont += 1
    pesoTotal += peso
    alturaTotal += altura

    if cont == 1:
        maior, codMaior = altura, cod
        menor, codMenor = altura, cod
        maisGordo, codGordo = peso, cod
        maisMagro, codMagro = peso, cod

    else:
        if altura > maior:
            maior, codMaior = altura, cod
        if altura < menor:
            menor, codMenor = altura, cod
        if peso > maisGordo:
            maisGordo, codGordo = peso, cod
        if peso < maisMagro:
            maisMagro, codMagro = peso, cod

print(f"""
Maior cliente:
    Código: {codMaior}
    Altura: {maior} m

Menor cliente:
    Código: {codMenor}
    Altura: {menor} m

Cliente mais pesado:
    Código: {codGordo}
    Peso: {maisGordo} Kg

Cliente mais leve:
    Código: {codMagro}
    Peso: {maisMagro} Kg


Total de Clientes: {cont}
Média dos pesos: {pesoTotal/cont:.2f} Kg
Médis das alturas: {alturaTotal/cont:.2f} m

""")
