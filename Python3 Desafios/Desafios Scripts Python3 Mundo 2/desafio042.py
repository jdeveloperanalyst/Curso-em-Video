# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print("-=" * 30)
print("Analisador de Triângulos")
print("-=" * 30)

reta1 = float(input("\nPrimeiro segmento: "))
reta2 = float(input("Segundo segmento: "))
reta3 = float(input("Terceiro segmento: "))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta1 + reta3 > reta2:
    print("Os segmentos acima PODEM FORMAR um triângulo!")
else:
    print("Os segmentos acima NÁO PODEM FORMAR um triângulo!")
