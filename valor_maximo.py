# from array import *
# from math import *

# alpha = array('i', [100, 200, 300, 400, 500, 600, 700, 800])

# def find_max(arr):
#   return(find_max)

# print(f"O maior número é o: {find_max} ")
       
from array import *
from math import *

lista = array('i', [100, 200, 300, 400, 500, 600, 700, 800])  # Corrected array initialization

def find_max(arr):
    max_num = arr[0]  # Initialize with the first element
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num  # Return the maximum number, not the function itself

max_valor = find_max(lista) # Call the function and store the result

print(f"O maior número é o: {max_valor}") # Print the stored result