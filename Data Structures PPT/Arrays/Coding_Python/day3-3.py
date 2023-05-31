"""
Question 3
Given an array arr[] of distinct elements size N that is sorted and then around an
unknown point, the task is to check if the array has a pair with a given sum X.
Examples :
Input: arr[] = {11, 15, 6, 8, 9, 10}, X = 16
Output: true
Explanation: There is a pair (6, 10) with sum 16

Solution:
Java: https://pastebin.com/Qiwq93mT
Python: https://pastebin.com/uXaUAuS5
Javascript: https://pastebin.com/dP7iFnsB
Time Complexity: O(n), where n is the length of the input array.
Space Complexity: O(1).

"""
"""
def find_pair(arr, x):
    n = len(arr)
    # find pivot element
    pivot = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            pivot = i + 1
            break
    left = pivot
    right = pivot - 1
    while left != right:
        if arr[left] + arr[right] == x:
            return True
        elif arr[left] + arr[right] < x:
            left = (left + 1) % n
        else:
            right = (right - 1 + n) % n
    return False
 
arr = [11, 15, 6, 8, 9, 10]
x = 16
print(find_pair(arr, x))
 

"""
def find_pair(arr,x):
    min_index=0
    max_index=0
    for i in range(len(arr)):
        if arr[i]<arr[min_index]:
            min_index = i
        elif arr[i]>arr[max_index]:
            max_index=i
    low = min_index
    high = max_index
    n=len(arr)
    while low!=high:
        if  arr[low]+arr[high]>x:
            high = (high-1+n)%n
        elif arr[low]+arr[high]<x:
            low = (low+1)%n 
        elif arr[low]+arr[high]==x:
            return [arr[low],arr[high]]
    return -1


print(find_pair([11,15,6,8,9,10], 20))

    