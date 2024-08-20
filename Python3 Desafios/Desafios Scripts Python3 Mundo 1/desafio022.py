# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome_completo = str(input("\nDigite seu nome completo: "))

print("\nAnalisando seu nome...")
print(f"Seu nome em maiúsculas é {nome_completo.upper()}.")
print(f"Seu nome em minúsculas é {nome_completo.lower()}.")
print(f'Seu nome tem ao todo {len(nome_completo.replace(" ", ""))} letras.')
print(f"Seu primeiro nome é {nome_completo.split()[0]} e ele tem {len(nome_completo.split()[0])} letras.\n")
