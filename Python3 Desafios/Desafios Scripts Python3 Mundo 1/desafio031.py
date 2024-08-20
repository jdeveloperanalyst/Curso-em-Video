# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Informe qual é a distância da sua viagem? "))

print(f"Você está prestes a realizar uma viagem de {distancia}Km.")

if distancia <= 200:
    preco = distancia * 0.50
    passagem = f"{preco:.2f}"
else:
    preco = distancia * 0.45
    passagem = f"{preco:.2f}"

print(f"E o valor da sua passagem é R${passagem.replace('.', ',')}")
