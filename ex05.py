################################################################
# Descrição: Calcula a média de duas notas parciais e          #
#            determina a situação de aprovação do aluno.       #
# Parâmetros de entrada: Duas notas parciais (números reais).  #
# Valores de saída: Mensagem "Aprovado", "Reprovado" ou        #
#                   "Aprovado com Distinção".                  #
# Autor: Miguel Duccini Cunha de freitas                       #
################################################################

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
  print("Aprovado com Distinção")
elif media >= 7:
  print("Aprovado")
else:
  print("Reprovado")