# Solicitamos o primeiro número ao usuário e armazenamos na variável "numero1".
# A função input() recebe o valor digitado pelo usuário (que é sempre uma string)
# e a função float() converte essa string para um número decimal.
numero1 = float(input("Digite o primeiro número: "))

# Solicitamos o segundo número ao usuário e armazenamos na variável "numero2".
numero2 = float(input("Digite o segundo número: "))

# Aqui, realizamos a operação de soma (+) entre os dois números.
resultado = numero1 + numero2

# Exibimos o resultado da soma para o usuário.
print("A soma de", numero1, "e", numero2, "é:", resultado)