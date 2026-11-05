################################################################
# Descrição: Apresenta o somatório dos valores pares           #
#            existentes na faixa de 1 até 500.                 #
# Parâmetros de entrada: Nenhum.                               #
# Valores de saída: O valor da soma dos números pares no       #
#                   intervalo.                                 #
# Autor: Miguel Duccini Cunha de Freitas                       #
################################################################

soma_pares = 0
for i in range(1, 501):
  if i % 2 == 0:
    soma_pares += i

print(f"O somatório dos valores pares de 1 até 500 é: {soma_pares}")