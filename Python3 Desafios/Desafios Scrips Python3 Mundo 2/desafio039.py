# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = 2017  # datetime.now().year
idade = ano_atual - ano_nascimento

print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.")

if idade < 18:
    print(f"Ainda faltam {18 - idade} anos para o alistamento.")
    print(f"Seu alistamento será em {ano_atual + (18 - idade)}.")
elif idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade > 18:
    print(f"Você já deveria ter se alistado há {idade - 18} anos.")
    print(f"Seu alistamento foi em {ano_atual + (18 - idade)}.")
