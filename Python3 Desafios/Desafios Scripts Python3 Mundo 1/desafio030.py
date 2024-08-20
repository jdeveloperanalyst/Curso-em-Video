# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input("\033[0;35mInforme um número qualquer: \033[m"))

if numero % 2 == 0:
    print(f"O número {numero} é \033[0;34mPAR\033[m")
else:
    print(f"O número é \033[0;34mÍMPAR\033[m")
