def rotate_matrix(matrix):
    copied_mat = [[element for element in row] for row in matrix]
    rows = len(matrix)-1
    cols = len(matrix[0])-1
    for i in range(rows,-1,-1):
        for j in range(cols+1):
            matrix[j][rows-i] = copied_mat[i][j]
    return matrix
print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))