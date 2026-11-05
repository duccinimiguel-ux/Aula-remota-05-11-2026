################################################################
# Descrição: Calcula e apresenta a soma dos cem primeiros      #
#            números naturais (1 a 100).                       #
# Parâmetros de entrada: Nenhum.                               #
# Valores de saída: O valor total da soma acumulada.           #
# Autor: Miguel Duccini Cunha de Freitas                       #
################################################################

soma = 0
for i in range(1, 101):
  soma += i

print(f"A soma dos 100 primeiros números naturais é: {soma}")