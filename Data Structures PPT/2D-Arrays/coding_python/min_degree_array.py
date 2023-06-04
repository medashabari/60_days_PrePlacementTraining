"""
<aside>
💡 ******************Question 4******************

Given a non-empty array of non-negative integers nums, the **degree** of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

**Example 1:**

**Input:** nums = [1,2,2,3,1]

**Output:** 2

**Explanation:**

The input array has a degree of 2 because both elements 1 and 2 appear twice.

Of the subarrays that have the same degree:

[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]

The shortest length is 2. So return 2.

**************************************Complexity Analysis**************************************

- Time Complexity: O(m*n)
- Space Complexity: O(1)
</aside>
"""

def min_size_max_degree_arr(nums):
    left={}
    right={}
    freq={}

    for i in range(len(nums)):
        if nums[i] not in left:
            left[nums[i]]=i

        right[nums[i]]=i
        freq[nums[i]] = freq.get(nums[i],0)+1

        ans=len(nums)
        max_len = max(freq.values())  

    for key,value in freq.items():
        if value == max_len:
            ans = min(ans,abs(left[key]-right[key])+1) 

    return ans

print(min_size_max_degree_arr([1,2,2,3,1]))
    

    
