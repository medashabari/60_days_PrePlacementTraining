"""
**Q1.** Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.

**Examples:**

Input: arr[] = {3, 5, 4, 1, 9}

Output: Minimum element is: 1

Maximum element is: 9

**Solution:**

**Java**

Code Link :- https://pastebin.com/hMGGWh8h

**Python**

Code link :- https://pastebin.com/QY1F14zj

**Javascript**

Code link :- https://pastebin.com/jSwAgcUU

TC : O(n)

SC: O(n)
"""

class Pair:
    def __init__(self):
        self.min=0
        self.max=0
 
def getMinMax(arr:list,n:int) -> Pair:
    minmax=Pair()
    
    # if only one element in array
    if n==1:
        minmax.min=arr[0]
        minmax.max=arr[0]
    # if only 2 elements in array
    if arr[0]>arr[1]:
        minmax.min=arr[1]
        minmax.max=arr[0]
    else:
        minmax.min=arr[0]
        minmax.max=arr[1]
    
    # if more than 2 elements
    for i in range(2,n):
        if arr[i]>minmax.max:
            minmax.max=arr[i]
        elif arr[i]<minmax.min:
            minmax.min=arr[i]
    
    return minmax

if __name__ == '__main__':
    arr = list(map(int,input("Enter elemenets").split()))
    n = len(arr)
    minmax = getMinMax(arr,n)
    print(f"Minimum Element is {minmax.min}\nMaximum element is {minmax.max}")
