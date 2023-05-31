"""
Question 6
Given a binary array nums, return the maximum number of consecutive 1's in the
array.
Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The
maximum number of consecutive 1s is 3.
Solution:
Java: https://pastebin.com/efc2VPCa
Python: https://pastebin.com/TniaKBBH
Javascript: https://pastebin.com/Wxaj7wut
TC : O(n)
SC : O(1)
"""
def max_consective_ones(arr):
    counter=0
    max_length=1

    for i in arr:
        if i==1:
            counter+=1
        elif i==0:
            max_length=max(max_length,counter)
            counter=0
    return max_length

print(max_consective_ones([1,1,0,1,0,1,0]))