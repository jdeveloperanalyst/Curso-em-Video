# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome_completo = str(input("\nDigite seu nome completo: ")).strip()

print("\nMuito prazer em te conhecer!")
print(f"Seu primeiro nome é {nome_completo.split()[0]}.")
print(f"Seu último nome é {nome_completo.split()[-1]}.")
