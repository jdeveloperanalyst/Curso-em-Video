# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
# ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

nomes = [
    str(input("Primeiro aluno: ")),
    str(input("Segundo aluno: ")),
    str(input("Terceiro aluno: ")),
    str(input("Quarto aluno: ")),
]

print(f"O aluno escolhido foi {choice(nomes)}.")
