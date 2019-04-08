# coding: utf-8

# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input("Digite um número: "))

a = 1
b = 1

for i in range(n):
    print(a)
    a, b = b, a+b
