# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
# a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("\nQual é o salário do funcionário? R$"))

if salario <= 1250:
    aumento = salario + ((salario * 15) / 100)
else:
    aumento = salario + ((salario * 10) / 100)

salario_atual = f"{salario:.2f}"
aumento_salario = f"{aumento:.2f}"
print(f"Quem ganhava R${salario_atual.replace('.', ',')} passa a ganhar R${aumento_salario.replace('.', ',')} agora.\n")
