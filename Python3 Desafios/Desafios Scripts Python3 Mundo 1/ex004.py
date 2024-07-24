# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

obj = input("Digite algo: ")

print(f"O tipo primitivo desse valor é {type(obj)}")
print(f"Só tem espaços? {obj.isspace()}")
print(f"É um número? {obj.isnumeric()}")
print(f"É alfabético? {obj.isalpha()}")
print(f"É alfanumérico? {obj.isalnum()}")
print(f"Está em maiúsculas? {obj.isupper()}")
print(f"Está em minúsculas? {obj.islower()}")
print(f"Está capitalizada? {obj.istitle()}")
print()
