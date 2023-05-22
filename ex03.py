#
# autores:
# Cristiano, Michel
# 
# Data: 22/05/2023
# #
# 
# 3 - Faça um algoritmo que receba dez números inteiros do usuário e exiba qual o maior número informado.
###
# entrada de dados
maior = 0
for i in range(1, 11):
    valor = int(input("Digite um valor: "))
    if valor > maior:
        maior = valor
# saída de dados
print(f"O maior valor é {maior}")
print("Fim do programa")
