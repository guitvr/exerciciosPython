# coding: utf-8

# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo

s = str(input("Digite seu sexo: ")).lower()

if s == "m":
    print("Sexo M - Masculino")
elif s == "f":
    print("Sexo F - Feminino")
else:
    print("Opção inválida")
