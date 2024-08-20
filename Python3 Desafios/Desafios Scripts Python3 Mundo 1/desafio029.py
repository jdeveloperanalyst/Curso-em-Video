# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade_do_carro = float(input("\nInforme a velocidade: "))

if velocidade_do_carro > 80:
    print(f"\033[0;31mMULTADO! Você excedeu o limite permitido que é de 80Km/h.\033[m")

    calculo_multa = float(velocidade_do_carro - 80) * 7
    multa = f"{calculo_multa:.2f}"

    print(f"\033[0;31mVocë deve pagar uma multa de\033[m \033[0;33mR${multa.replace('.', ',')}!\033[m")

print("\033[0;32mTenha um bom dia! Dirija com segurança!\033[m")
