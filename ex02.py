#
# autores:
# Cristiano, Michel
# 
# Data: 22/05/2023
# #
# 
# 2 – Faça programa que calcule o fatorial de um número.
###
# entrada de dados
valor =  input("Digite um valor: ")
fatorial = 1

# processamento
for i in range(1, int(valor) + 1):
    fatorial = fatorial * i 
    
# saída de dados
print(f"O fatorial de {valor} é {fatorial}")
print("Fim do programa")

# 3 – Faça um programa que calcule o fatorial de um número usando o comando while.
###
# entrada de dados
valor =  input("Digite um valor: ")
fatorial = 1

# processamento
i = 1
while i <= int(valor):
    fatorial = fatorial * i 
    i = i + 1
    
# saída de dados
print(f"O fatorial de {valor} é {fatorial}")


