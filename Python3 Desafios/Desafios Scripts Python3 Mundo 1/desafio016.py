# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção
# Inteira.

import math

valor = float(input("Digite um valor: "))

print(f"O valor digitado foi {valor} e sua porção inteira é {math.trunc(valor)}")
