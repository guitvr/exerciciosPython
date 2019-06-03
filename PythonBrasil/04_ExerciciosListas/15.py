# coding: utf-8

# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada
# de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

notas = []

while True:
    n = float(input("Digite uma nota (nota < 0 para encerrar): "))

    if n < 0:
        break

    notas.append(n)


soma = sum(notas)
media = soma/len(notas)
qntAcimaMedia = 0
qntAbaixo7 = 0

for n in notas:
    qntAcimaMedia += 1 if n > media else 0
    qntAbaixo7 += 1 if n < 7 else 0


print("\nNotas (na ordem que foram digitadas): ")
for n in notas:
    print(n, end=' ')

print("\nNotas (na ordem inversa à que foram informados): ")
for n in reversed(notas):
    print(n)

print(f"""
Soma: {sum(notas)}
Média: {sum(notas)/len(notas):.1f}
Quantidade de notas acima da média: {qntAcimaMedia}
Quantidade de notas abaixo de 7: {qntAbaixo7}
""")

print("Programa encerrado")
