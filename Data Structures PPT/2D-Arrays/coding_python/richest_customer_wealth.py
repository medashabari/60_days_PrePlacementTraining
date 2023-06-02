"""
Richest customer wealth
[[1,2,3],[3,2,1]]
1st customer 1+2+3 = 6
2nd customer 3+2+1 = 6
"""

def richest_customer_wealth(matrix):
    max_wealth = 0
    for row in matrix:
        curr_wealth = sum(row)

        max_wealth = max(curr_wealth,max_wealth)
    return max_wealth

rows=int(input("Enter number of rows "))
cols=int(input("Enter number of columns "))

matrix = [[int(input()) for col in range(cols)] for row in range(rows)]
print(richest_customer_wealth(matrix))