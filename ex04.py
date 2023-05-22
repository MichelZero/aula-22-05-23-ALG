#
# autores:
# Cristiano, Michel
# 
# Data: 22/05/2023
# #
# 
# 4 - Elabore um algoritmo que recebe um texto do usuário e informe 
# quantas vogais estão presentes neste texto.

###
# entrada de dados  
texto = input("Digite um texto: ")
vogais = 0
# processamento
for letra in texto: 
    if letra in "aeiou":
        vogais = vogais + 1
# saída de dados
print(f"O texto tem {vogais} vogais")
print("Fim do programa")

