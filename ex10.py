################################################################
# Descrição: Apresenta todos os valores numéricos inteiros     #
#            ímpares situados na faixa de 0 a 20.              #
# Parâmetros de entrada: Nenhum.                               #
# Valores de saída: Os números ímpares impressos um a um.      #
# Autor: Miguel Duccini Cunha de Freitas                       #
################################################################

print("Valores ímpares de 0 a 20:")
for i in range(0, 21):
  if i % 2 != 0:  # Verifica se o resto da divisão por 2 é diferente de zero
    print(i)