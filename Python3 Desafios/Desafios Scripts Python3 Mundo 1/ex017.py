# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo. Calcule e mostre o comprimento da hipotenusa.

import math as m

cateto_oposto = float(input("\nComprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = m.sqrt((pow(cateto_oposto, 2) + pow(cateto_adjacente, 2)))

print(f"A hipotenusa vai medir {hipotenusa:.2f}\n")


# Outra forma

cateto_oposto = float(input("\nComprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = (cateto_oposto**2 + cateto_adjacente**2) ** (1 / 2)

print(f"A hipotenusa vai medir {hipotenusa:.2f}\n")


# Outra forma

cateto_oposto = float(input("\nComprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = m.hypot(cateto_oposto, cateto_adjacente)

print(f"A hipotenusa vai medir {hipotenusa:.2f}\n")
