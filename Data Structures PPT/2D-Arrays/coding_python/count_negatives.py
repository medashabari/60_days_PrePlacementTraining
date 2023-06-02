"""
Count negative numbers in a matrix where sorted in decresing order both row and column wise

4 3 2 -1
3 2 1 -1
1 1 -1 -1
-1 -1 -2 -3

op 8
"""

from typing import List
def count_negatives(matrix:List[List[int]]):
    count=0 
    n=len(matrix[1])

    for row in matrix:
        low=0
        high=len(row)-1
        while low<=high:
            mid = (low+high)//2
            if row[mid] <0:
                high = mid-1
            else:
                low=mid+1
        count+=n-low
    return count




rows=int(input("Enter number of rows "))
cols=int(input("Enter number of columns "))

matrix = [[int(input()) for col in range(cols)] for row in range(rows)]

print(count_negatives(matrix))