#desafio 2°
# Solicita ao usuário a string
string = input("Digite a string: ")

# Solicita ao usuário o número de repetições
numero_repeticoes = int(input("Digite o número de vezes para repetir a string: "))

# Verifica se o número de repetições é válido
if numero_repeticoes < 0:
    print("O número de repetições deve ser um inteiro não negativo.")
else:
    # Repete a string o número de vezes informado
    resultado = string * numero_repeticoes

    # Imprime o resultado
    print("A string repetida", numero_repeticoes, "vezes é:", resultado)