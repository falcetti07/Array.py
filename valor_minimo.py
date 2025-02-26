from array import *
from math import *

lista = array('i', [100, 200, 300, 400, 500, 600, 700, 800])

def find_min(arr):
  min_num = arr[0]
  for num in arr:
    if num < min_num:
      min_num = num
  return min_num

min_valor = find_min(lista)
print(f'O menor número da lista é o:{min_valor}')
    
