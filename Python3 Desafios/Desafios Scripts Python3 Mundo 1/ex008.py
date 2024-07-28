# Escreva um programa que leia um valor em medida e o exiba convertido em centímedida e milímedida.

medida = int(input("Uma distância em medida: "))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

resultado = f"""A medida de {medida} corresponde á:
{km}km (Quilômetros)
{hm}hm  (Hectômetros)
{dam}dam  (Decâmetros)
{dm}dm    (Decímetros)
{cm}cm   (Centímetros)
{mm}mm  (Milímetros)
"""

print(resultado)
