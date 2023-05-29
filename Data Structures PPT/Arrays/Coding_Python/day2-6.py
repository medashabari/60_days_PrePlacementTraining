"""
Question 6
There are many situations where we use integer values as index in array to see
presence or absence. We can use bit manipulations to optimize space in such
problems.
Let us consider the below problem as an example.
Given two numbers say a and b, mark the multiples of 2 and 5 between a and b
and output each of the multiples.
Note : We have to mark the multiples i.e save (key, value) pairs in memory such
that each key either has a value as 1 or 0 representing a multiple of 2 or 5 or not
respectively.
Examples :
Input : 2 10
Output : 2 4 5 6 8 10
Input: 60 95
Output: 60 62 64 65 66 68 70 72 74 75 76 78
80 82 84 85 86 88 90 92 94 95

Solution:
Java: https://pastebin.com/14gqxY5W
Python: https://pastebin.com/jYse75qN
Javascript: https://pastebin.com/PxRpLKyK
TC : O (n)
SC : O(n)
"""

def main():
    a = 60
    b = 70
    size = abs(b - a) + 1
    array = [0] * size
 
    for i in range(a, b + 1):
        if i % 2 == 0 or i % 5 == 0:
            array[i - a] = 1
 
    for i in range(a, b + 1):
        if array[i - a] == 1:
            print(i, end=' ')
 
if __name__ == '__main__':
    main()