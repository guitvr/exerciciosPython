# coding: utf-8

# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#   Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#   Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#   A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
#
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa
# permitindo que o usuário digite o salário inicial do funcionário.

from datetime import date

anoAtual = date.today().year

# Em 1995
salarioInicial = float(input("Digite o salário inicial: R$"))

# Em 1996
aumento = 0.015
salario = aumento*salarioInicial + salarioInicial

# A partir de 1997 (inclusive)
for i in range(1997, anoAtual+1):
    aumento *= 2
    salario = aumento * salario + salario
    print(f"Aumento: {aumento*100}% em {i} | salário: R$ {salario:.2f}")
