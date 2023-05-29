"""
Question 4
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You
may assume that the majority element always exists in the array.
Example 1:
Input: nums = [3,2,3]
Output: 3
Solution:
Java: https://pastebin.com/mVJL4PDB
Python: https://pastebin.com/E3AR6D6M
Javascript: https://pastebin.com/uQipiegQ
TC: O(nlogn)
SC : O(logn)
"""

"""class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]

sol = Solution()
print(sol.majorityElement([2,3,1,3,2,2,4,12,1,2,2,2,3,3,3,3,3,3,3]))"""


def majorityElement(nums):
    frequency_counter={}
    for i in nums:
        if i in frequency_counter:
            frequency_counter[i]+=1
            if frequency_counter[i] > len(nums)//2:
                return i 
        else:
            frequency_counter[i]=1
print(majorityElement([3,2,3]))