# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do
# comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Valor da casa: R$"))
salario_comprador = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento? "))
prestacao = valor_casa / (anos * 12)
print(f"Para pagar uma casa de R${valor_casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}")
if prestacao > (salario_comprador * (30 / 100)):
    print("Empréstimo NEGADO!\n")
else:
    print("Empréstimo pode ser CONCEDIDO!\n")
