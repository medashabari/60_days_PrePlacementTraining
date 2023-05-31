"""
Given a m * n matrix, traverse the matrix in sprial order and print elements

1 2 3
4 5 6
7 8 9

1 -> 2 -> 3
           |
4 ->   5   6
|          |
7 <-   8 <-9

op = 1 2 3 6 9 8 7 4 5
"""

from typing import List
def sprial_traversal(matrix:List[List[int]]) -> List:
    res=[]
    top , left = 0 , 0
    bottom, right = len(matrix[0])-1,len(matrix[1])-1
    while left <= right and top <= bottom: 
        # top most row left to right
        for i in range(left,right+1):
            res.append(matrix[left][i])
        top+=1
        
        # right most row top to bottom
        for i in range(top,bottom+1):
            res.append(matrix[i][bottom])
        right-=1

        # bottom row right to left
        if top<=bottom:
            for i in range(right,left-1,-1):
                res.append(matrix[bottom][i])
            bottom-=1
        # left most row bottom to top
        if left <= right:
            for i in range(bottom,top-1,-1):
                res.append(matrix[i][left])
            left+=1
    return res 


rows=int(input("Enter number of rows "))
cols=int(input("Enter number of columns "))

matrix = [[int(input()) for col in range(cols)] for row in range(rows)]
    
print(sprial_traversal(matrix))

