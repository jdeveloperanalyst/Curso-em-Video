from random import randint

print(
    """[1] - PEDRA
[2] - PAPEL
[3] - TESOURA
Qual a sua jogada? """
)

itens = [None, "PEDRA", "PAPEL", "TESOURA"]
t800 = randint(1, 3)
jogador = int(input("Qual é a sua jogada? "))
print(itens[jogador])
print(itens[t800])

if itens[jogador] == "PEDRA":
    if itens[t800] == "PEDRA":
        print("EMPATOU...")
        print(f"Você Jogou {itens[jogador]} e a maquina {itens[t800]}!")
    elif itens[t800] == "PAPEL":
        print("VOCÊ PERDEU...")
        print(f"Você jogou {itens[jogador]} e a maquina {itens[t800]}!")
    elif itens[t800] == "TESOURA":
        print("VOCÊ GANHOU...")
        print(f"Você jogou {itens[jogador]} e a maquina {itens[t800]}!")
elif itens[jogador] == "PAPEL":
    if itens[t800] == "PAPEL":
        print("EMPATOU...")
        print(f"Você Jogou {itens[jogador]} e a maquina {itens[t800]}!")
    elif itens[t800] == "TESOURA":
        print("VOCÊ PERDEU...")
        print(f"Você jogou {itens[jogador]} e a maquina {itens[t800]}!")
    elif itens[t800] == "PEDRA":
        print("VOCÊ GANHOU...")
        print(f"Você jogou {itens[jogador]} e a maquina {itens[t800]}!")
elif itens[jogador] == "TESOURA":
    if itens[t800] == "TESOURA":
        print("EMPATOU...")
        print(f"Você Jogou {itens[jogador]} e a maquina {itens[t800]}!")
    elif itens[t800] == "PEDRA":
        print("VOCÊ PERDEU...")
        print(f"Você jogou {itens[jogador]} e a maquina {itens[t800]}!")
    elif itens[t800] == "PAPEL":
        print("VOCÊ GANHOU...")
        print(f"Você jogou {itens[jogador]} e a maquina {itens[t800]}!")
