# coding: utf-8

# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

consoantes = "bcdfghjklmnpqrstvwxyz"
vogais = "aeiou"

letra = str(input("Digite uma letra: ")).lower().strip()
letra = letra[0]

if letra in vogais:
    print(f"'{letra}' é vogal")
elif letra in consoantes:
    print(f"'{letra}' é consoante")
else:
    print(f"'{letra}' não é vogal e nem consoante")
