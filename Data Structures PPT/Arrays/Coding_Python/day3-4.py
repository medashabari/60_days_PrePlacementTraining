"""
Question 4
Given an array nums with n objects colored red, white, or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order red,
white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue,
respectively.
You must solve this problem without using the library's sort function.
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Solution:
Java: https://pastebin.com/1Ww9Ayva
Python: https://pastebin.com/hU0cv236
Javascript: https://pastebin.com/46w0pjc3
TC : O(n)
SC : O(1)
"""

def sort_colors(arr):
    p0=0
    curr=0
    p2=len(arr)-1

    while curr<=p2:
        if arr[curr]==0:
            arr[p0],arr[curr]=arr[curr],arr[p0]
            p0+=1
            curr+=1
        elif arr[curr]==2:
            arr[p2],arr[curr]=arr[curr],arr[p2]
            p2-=1
        else:
            curr+=1
    return arr

print(sort_colors([0,1,0,1,2,1,2,0,2]))