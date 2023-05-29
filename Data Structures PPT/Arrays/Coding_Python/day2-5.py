"""
Question 5
Given an array of integers nums containing n + 1 integers where each integer is in
the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only
constant extra space.
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2
Solution:
Java: https://pastebin.com/iAeDYGKd
Python: https://pastebin.com/vauPf0Yb
Javascript: https://pastebin.com/CQ0V3Q9u
TC : O(n)
SC : O(n)
"""
class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1