#```python
################################################################
# Descrição: digitar dois valores e imprimir o maior valor     #
# Parâmetros de entrada: números                               #
# Valores de saída: o maior valor digitado                     #
# Autor: Miguel Duccini Cunha de Freitas                        #
################################################################

print('Bem vindo ao programa!!')
num = []

for l in range (2):
    val = int(input(f'Digite o {l+1}° valor: '))
    num.append(val)

mai = max(num)

print(f'o maior valor digitado foi {mai}')