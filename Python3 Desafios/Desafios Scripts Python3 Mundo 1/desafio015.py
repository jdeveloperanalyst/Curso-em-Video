# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$60 por dia e R$0,15 por Km rodado.

dias_alugados = int(input("Quantos dias alugados? "))
km_rodados = float(input("Quantos Km rodados? "))

total_pagamento = (dias_alugados * 60) + (km_rodados * 0.15)

print(f"O total a pagar é de R${total_pagamento:.2f}")
