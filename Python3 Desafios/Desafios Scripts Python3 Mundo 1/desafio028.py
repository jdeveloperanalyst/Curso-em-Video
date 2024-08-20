# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

robo = randint(0, 5)

print("\033[0;33m-=\033[m" * 30)
print("\033[0;34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m")
print("\033[0;33m-=\033[m" * 30)

jogador = int(input("Em que número eu pensei? "))

print("\033[0;35mPROCESSANDO...\033[m")
sleep(3)
if jogador == robo:
    print("\033[0;32mPARABÉNS! Você conseguiu me vencer!\033[m\n")
else:
    print(f"\033[0;31mGANHEI! Eu pensei no número {robo} e não no {jogador}!\033[m\n")
