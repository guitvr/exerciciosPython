# coding: utf-8

# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média
# anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ["Janeiro",
         "Fevereiro",
         "Março",
         "Abril",
         "Maio",
         "Junho",
         "Julho",
         "Agosto",
         "Setembro",
         "Outubro",
         "Novembro",
         "Dezembro"
         ]

tempMediaMeses = []

for m in range(12):
    tempMediaMeses.append(float(input(f"Digite a temperatura média do mês de {meses[m]} (em °C): ")))

mediaAnual = sum(tempMediaMeses) / 12

print(f"\nMédia anual: {mediaAnual:.2f} °C")
print("Meses com temperaturas acima da média:")

for i in range(12):
    if tempMediaMeses[i] > mediaAnual:
        print(f"{meses[i]}: {tempMediaMeses[i]} °C")
