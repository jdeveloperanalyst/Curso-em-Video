# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))

if valor1 > valor2:
    print("O PRIMEIRO valor é MAIOR.")
elif valor2 > valor1:
    print("O SEGUNDO valor é MAIOR.")
else:
    print("Os dois valores são IGUAIS.")
