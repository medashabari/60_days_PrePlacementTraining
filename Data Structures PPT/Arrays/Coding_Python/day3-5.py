"""
Question 5
Given an integer array nums, rotate the array to the right by k steps, where k is
non-negative.
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Solution:
Java: https://pastebin.com/A2946y15
Python: https://pastebin.com/sKMwrVD7
Javascript: https://pastebin.com/JRePFGWE
TC: O(n)
SC: O(1)
"""
"""def rotate_arr(arr,k):
    return arr[-k:]+arr[:-k]"""

def rotate_arr(arr,k):
    k=k%len(arr)
    reverse(arr,0,len(arr)-1)
    reverse(arr,0,k-1)
    reverse(arr,k,len(arr)-1)
    return arr

def reverse(arr,i,j):
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

print(rotate_arr([1,2,3,4,5,6,7], 3))