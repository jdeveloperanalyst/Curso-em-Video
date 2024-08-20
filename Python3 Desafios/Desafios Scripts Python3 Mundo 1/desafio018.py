# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse ângulo.

import math

valor = float(input("\nDigite o ângulo que você deseja: "))
angulo = math.radians(valor)
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print(f"O Angulo de {angulo:.1f} tem o SENO de {seno:.2f}")
print(f"O Angulo de {angulo:.1f} tem o COSSENO de {cosseno:.2f}")
print(f"O Angulo de {angulo:.1f} tem o TANGENTE de {tangente:.2f}\n")
