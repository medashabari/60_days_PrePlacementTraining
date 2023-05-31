"""
Givenn a sqaure matrix, return the sum of primary diagonal elements and secondary digoanl elements which are not part of primary

1 2 3
4 5 6
7 8 9

op = 1+5+7+3+9
"""

def sum_diagonal_elements(matrix,rows,cols):
    sum=0
    n=len(matrix)
    for i in range(len(matrix)):
        sum+=matrix[i][i]
        sum+=matrix[i][n-1-i]
    if n%2==1: # odd 
        sum-=matrix[n//2][n//2]

    return sum
rows=int(input("Enter number of rows "))
cols=int(input("Enter number of columns "))

matrix = [[int(input()) for col in range(cols)] for row in range(rows)]
    
print(sum_diagonal_elements(matrix,rows,cols))