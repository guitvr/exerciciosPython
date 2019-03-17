# coding: utf-8

# Faça um programa que leia e valide as seguintes informações:
#   Nome: maior que 3 caracteres;
#   Idade: entre 0 e 150;
#   Salário: maior que zero;
#   Sexo: 'f' ou 'm';
#   Estado Civil: 's', 'c', 'v', 'd';

nome = str(input("Nome: "))

while len(nome) <= 3:
    print("\nDigite um nome válido (mais de 3 caracteres)\n")
    nome = str(input("Nome: "))

idade = int(input("Idade: "))

while not (0 <= idade <= 150):
    print("\nDigite uma idade válida (entre 0 e 150 anos)\n")
    idade = int(input("Idade: "))

salario = float(input("Salário: "))

while salario <= 0:
    print("\nDigite um salário válido (maior que 0)\n")
    salario = float(input("Salário: "))

sexo = str(input("Sexo (M - Masculino ou F - Feminino): ")).lower()

while sexo not in 'mf':
    print("\nDigite um valor para sexo válido.\n")
    sexo = str(input("Sexo (M - Masculino ou F - Feminino): ")).lower()

estadoCivil = str(input("Estado Civil (S - Solteiro(a), C - Casado(a), V - Viúvo(a), D - Divorciado(a): ")).lower()

while estadoCivil not in 'scvd':
    print("\nDigite um valor para Estado Civil válido.\n")
    estadoCivil = str(input("Estado Civil (S - Solteiro(a), C - Casado(a), V - Viúvo(a), D - Divorciado(a): ")).lower()
