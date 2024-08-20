# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math as m

n = int(input("Digite um número: "))

dobro = n * 2
triplo = n * 3
raiz_quadrada = m.sqrt(n)

texto =f"""O dobro de {n} vale {dobro}
O triplo de {n} vale {triplo}
A raiz quadrada de {n} é i gual a {raiz_quadrada:.2f}
""" 

print(texto)