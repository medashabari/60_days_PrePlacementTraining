"""
Question 1
Given an array nums containing n distinct numbers in the range [0, n], return the
only number in the range that is missing from the array.
Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range
[0,3]. 2 is the missing number in the range since it does not appear in nums.
Solution:
Java: https://pastebin.com/ZdAM2s5J
Python: https://pastebin.com/HJ2sXVbV
Javascript: https://pastebin.com/JJr1RvBt
TC: O(n)
SC: O (n)
"""
class Solution:
    def missingNumber(self, nums):
        numSet = set(nums)
 
        expectedNumCount = len(nums) + 1
        for number in range(expectedNumCount):
            if number not in numSet:
                return number
 
        return -1