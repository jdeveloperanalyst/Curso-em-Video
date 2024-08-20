# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela
# pode comprar.

valor_real = float(input("Quando dinheiro você tem na carteira? R$"))

valor_dolar = valor_real / 3.27

print(f"Com R${valor_real} você pode comprar US${valor_dolar:.2f}")
