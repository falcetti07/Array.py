from array import *
from math import *

matrizA = [ [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
          ]
def show(matrix):
     s="\n"
     # print array
     if not (isinstance(matrix[0],list)):
          linha = "\t"  
          for e in matrix:
               linha += str(e)+'\t'
          s+=linha+"\n"
     else:
          # print matrix          
          m = len(matrix)
          n = len(matrix[0])
          for i in range(m):
               linha = '\t'
               for j in range(n):
                  linha += str(matrix[i][j]) + '\t'
               s+=linha+"\n"
     print(s)