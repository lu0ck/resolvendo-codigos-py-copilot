# Solicitamos ao usuário que digite um número inteiro.
numero = int(input("Digite um número inteiro: "))

# Verificamos se o número é par ou ímpar usando o operador de módulo (%).
# O operador de módulo retorna o resto da divisão de um número por outro.
# Se o resto da divisão por 2 for 0, o número é par. Caso contrário, é ímpar.
if numero % 2 == 0:
    print(numero, "é um número par.")
else:
    print(numero, "é um número ímpar.")