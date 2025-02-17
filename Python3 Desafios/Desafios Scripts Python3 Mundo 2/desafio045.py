from random import randint
from time import sleep

print(
    """Suas opções:
[1] - PEDRA
[2] - PAPEL
[3] - TESOURA"""
)

itens = [None, "PEDRA", "PAPEL", "TESOURA"]
t800 = randint(1, 3)
jogador = int(input("Qual é a sua jogada? "))
# print(itens[jogador])
# print(itens[t800])

sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)

print("-=" * 11)
print(f"Você jogou {itens[jogador]} \ne a maquina {itens[t800]}!")
print("-=" * 11)

if itens[jogador] == "PEDRA":
    if itens[t800] == "PEDRA":
        print("EMPATOU...")
    elif itens[t800] == "PAPEL":
        print("VOCÊ PERDEU...")
    elif itens[t800] == "TESOURA":
        print("VOCÊ GANHOU...")
elif itens[jogador] == "PAPEL":
    if itens[t800] == "PAPEL":
        print("EMPATOU...")
    elif itens[t800] == "TESOURA":
        print("VOCÊ PERDEU...")
    elif itens[t800] == "PEDRA":
        print("VOCÊ GANHOU...")
elif itens[jogador] == "TESOURA":
    if itens[t800] == "TESOURA":
        print("EMPATOU...")
    elif itens[t800] == "PEDRA":
        print("VOCÊ PERDEU...")
    elif itens[t800] == "PAPEL":
        print("VOCÊ GANHOU...")
print()
