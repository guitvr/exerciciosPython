# coding: utf-8

# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
# ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

user = str(input("Nome de usuário: "))
pwd = str(input("Senha: "))

while pwd == user:
    print("\nSenha inválida. Não digite senha igual ao nome de usuário.\n")
    pwd = str(input("Senha: "))
