# coding: utf-8

# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade
# (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

qntMorangos = float(input("Digite a quantidade (em Kg) de morangos: "))
qntMacas = float(input("Digite a quantidade (em Kg) de maçãs: "))

precoMorangos = 2.5 * qntMorangos if qntMorangos <= 5.0 else 2.2 * qntMorangos
precoMacas = 1.8 * qntMacas if qntMacas <= 5.0 else 1.5 * qntMacas

total = precoMacas + precoMorangos

if qntMacas + qntMorangos >= 8 or precoMorangos + precoMacas >= 25.0:
    total = total - (total*0.1)

print(f"Total: R${total:.2f}")
