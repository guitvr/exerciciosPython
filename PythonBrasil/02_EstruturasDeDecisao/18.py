# coding: utf-8

# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = str(input("Digite uma data no formato dd/mm/aaaa: "))
if data.count("/") != 2:
    dataValida = False
else:
    data = data.split("/")
    dia, mes, ano = int(data[0]), int(data[1]), int(data[2])

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        diaBissexto = 29
    else:
        diaBissexto = 28

    mesDia = {1: 31, 2: diaBissexto, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if mes in mesDia.keys() and dia <= mesDia[mes]:
        dataValida = True
    else:
        dataValida = False

if dataValida:
    print("Data válida.")
else:
    print("Data inválida.")
