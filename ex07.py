################################################################
# Descrição: Mostra a tabuada tradicional de um número         #
#            informado pelo usuário (de 1 a 10).               #
# Parâmetros de entrada: Um número inteiro digitado pelo       #
#                        usuário.                              #
# Valores de saída: Linhas da tabuada tradicional do número.   #
# Autor: Miguel Duccini Cunha de Freitas                       #
################################################################

numero = int(input("Digite um número para ver a tabuada: "))

print(f"--- Tabuada do {numero} ---")
for i in range(1, 11):
  print(f"{numero} x {i} = {numero * i}")