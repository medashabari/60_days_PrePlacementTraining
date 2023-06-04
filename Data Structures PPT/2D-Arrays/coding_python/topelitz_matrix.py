"""
Given m * n matrix return True if the matrix is topelitz
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

1 2 3 4
5 1 2 3
9 5 1 2
output True

In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

"""

def topelitz_matrix(matrix):
    rows = len(matrix)-1
    cols = len(matrix[0])-1
    for i in range(rows):
        for j in range(cols):
            if i > 0 and j>0 and matrix[i-1][j-1]!=matrix[i][j]:
                return False 
    else:
        return True 


print(topelitz_matrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))