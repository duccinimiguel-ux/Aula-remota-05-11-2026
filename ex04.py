################################################################
# Descrição: Identifica o turno em que o aluno estuda com      #
#            base na letra informada (M, V ou N).              #
# Parâmetros de entrada: Letra correspondente ao turno         #
#                        (M, V ou N).                          #
# Valores de saída: Mensagem de cumprimento ("Bom Dia!",       #
#                   "Boa Tarde!", "Boa Noite!") ou             #
#                   "Valor Inválido!".                         #
# Autor: Miguel Duccini Cunha de Freitas                       #
################################################################

turno = (
    input("Digite o turno que você estuda (M, V ou N): ").strip().upper()
)

if turno == "M":
  print("Bom Dia!")
elif turno == "V":
  print("Boa Tarde!")
elif turno == "N":
  print("Boa Noite!")
else:
  print("Valor Inválido!")