# from array import *
# from math import *

# numeros = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# soma = 0

# def find_sum(arr):
#   global soma
#   for elemento in arr:
#      soma += elemento
#   return soma
  
# resultado = find_sum(numeros)
# print(f'A soma desse números é igual a {resultado}.')  



from array import *
from math import *

numeros = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
soma = 0  # Inicializa a variável soma ANTES da função

def find_sum(arr):
    global soma  # Indica que a variável soma é a global
    for elemento in arr:
        soma += elemento  # Acumula a soma dos elementos
    return soma

resultado = find_sum(numeros)
print(f'A soma desses números é igual a {resultado}.')
