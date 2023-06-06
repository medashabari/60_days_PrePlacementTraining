"""
write a funtion to reverse array of characters
tc= O(n)
sc=O(1)

Note must to do in inplace 
"""

def reverse_str(arr):
    left=0
    right=len(arr)-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left+=1
        right-=1
    return arr

print(reverse_str(['a','b','c','d']))