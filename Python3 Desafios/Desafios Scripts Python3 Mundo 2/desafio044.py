print("{:=^40}".format("LOJAS JONOVSKI"))

menu = """
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão 
Qual é a opção? """

preco_compras = float(input("Preço das compras: R$"))
opcao = int(input(menu))
if opcao == 1:
    total = preco_compras - (preco_compras * 10 / 100)
elif opcao == 2:
    total = preco_compras - (preco_compras * 5 / 100)
elif opcao == 3:
    total = preco_compras
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de {parcela:.2f} SEM JUROS.")
elif opcao == 4:
    total = preco_compras + (preco_compras * 20 / 100)
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print(f"Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS.")
else:
    total = preco_compras
    print("OPÇÃO INVALIDA de pagamento. Tente novamente!")
print(f"Sua compra de R${preco_compras:.2f} vai custar R${total:.2f} no final.")
