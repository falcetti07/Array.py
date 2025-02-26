def reverse(arr):
        pass

def find_max(arr):
        pass

def find_min(arr):
        pass

def find_sum(arr):
        pass

def palindromo(p1,p2):
        pass

def DNAtest(string):
        pass

def DNAoRNA(string):
        pass

def maxArea(height):
        pass

def printMatrixHadamard(matrix):
        if not matrix: return
        # print matrix
        n = len(matrix)
        for i in range(n): 
            linha=''
            for j in range(n): 
                if (matrix[i][j]):
                    linha+="T "
                else:
                    linha+="F "
            print(linha)
            
def Hadamard(n):
        pass

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
     
def main():
        arr=[-3000,100,240,120,-300,1000]
        print('arr  ',arr)
        print('reverse ',reverse(arr))
        print('max ',find_max(arr),'min ',find_min(arr))
        print('sum ',find_sum(arr),sum(arr))
        print('DNA  ','ACGTTA ', DNAtest('ACGTTA'))
        print('DNA : ','ACGT',' RNA :',DNAoRNA('ACGT'))
        height=[1,8,6,2,5,4,8,3,7]
        print('height :',height,'max area :',maxArea(height))
        height=[1,1]
        print('height :',height,'max area :',maxArea(height))
        height = [1,5,6,2,5,4,8,3]
        print('height :',height,'max area :',maxArea(height))
        print('Hadamard(4)')
        printMatrixHadamard(Hadamard(4))
        show([[1],[2]])
main()
