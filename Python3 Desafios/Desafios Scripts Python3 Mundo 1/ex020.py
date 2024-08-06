# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

nomes = [
    str(input("\nPrimeiro aluno: ")),
    str(input("Segundo aluno: ")),
    str(input("Terceiro aluno: ")),
    str(input("Quarto aluno: ")),
]

shuffle(nomes)

print(f"\nA ordem de apresentação será\n{nomes}\n")
