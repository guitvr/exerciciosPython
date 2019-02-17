# coding: utf-8

# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
# (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamArq = float(input("Digite o tamanho do arquivo (em MB): "))
velMbps = float(input("Digite a velocidade de um link de Internet (em Mbps): "))

velMBps = velMbps / 8
tempoMinutos = (tamArq / velMBps) / 60

print(f"\nTempo aproximado de download do arquivo usando este link: {tempoMinutos:.2f} minutos.")
