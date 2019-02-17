# coding: utf-8

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#   - comprar apenas latas de 18 litros;
#   - comprar apenas galões de 3,6 litros;
#   - misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os
#   valores para cima, isto é, considere latas cheias.

from math import ceil

area = float(input("Digite o valor da área a ser pintada (em metros quadrados): "))
tinta = area / 6
somenteLatas = {'qtd': ceil(tinta/18), 'valor': ceil(tinta/18) * 80}
somenteGaloes = {'qtd': ceil(tinta/3.6), 'valor': ceil(tinta/3.6) * 25}

tintaComFolga = tinta + tinta*0.1


qtdLatas = int(tintaComFolga / 18)
qtdGaloes = ceil((tintaComFolga % 18) / 3.6)
valorTotal = qtdLatas * 80 + qtdGaloes * 25

print(f"\nTinta necessária para os {area}m² : {tinta:.2f} litros")
print(f"\nApenas latas de 18 litros: R${somenteLatas['valor']:.2f} ({somenteLatas['qtd']} latas = "
      f"{somenteLatas['qtd']*18} litros)")
print(f"Apenas galões de 3,6 litros: R${somenteGaloes['valor']:.2f} ({somenteGaloes['qtd']} galões = "
      f"{somenteGaloes['qtd'] * 3.6} litros)")
print(f"Ou: R${valorTotal:.2f} ({qtdGaloes} galões + {qtdLatas} latas = {qtdLatas*18 + qtdGaloes*3.6} litros)")
