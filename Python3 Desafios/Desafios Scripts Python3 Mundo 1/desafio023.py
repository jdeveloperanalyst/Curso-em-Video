# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# exemplo:  3234
# unidade: 4
# dezenas: 3
# centenas: 2
# milhares: 3

num = int(input("\nDigite um número a ser fatiado: "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f"\nUnidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}\n")
