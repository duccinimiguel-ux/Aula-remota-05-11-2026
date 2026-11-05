################################################################
# Descrição: Verifica se uma letra digitada é "F" ou "M" e      #
#            informa se corresponde a Feminino, Masculino ou   #
#            se é um sexo inválido.                            #
# Parâmetros de entrada: Uma letra ("F" ou "M") digitada pelo  #
#                        usuário.                              #
# Valores de saída: Mensagem indicando "F - Feminino",           #
#                   "M - Masculino" ou "Sexo Inválido".        #
# Autor: Miguel Duccini Cunha de Freitas                       #
################################################################

sexo = input("Digite a letra (F ou M): ").strip().upper()

if sexo == "F":
  print("F - Feminino")
elif sexo == "M":
  print("M - Masculino")
else:
  print("Sexo Inválido")