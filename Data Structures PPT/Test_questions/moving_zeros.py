"""
Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
a. 1 <= nums.length <= 10^4
b. -2^31 <= nums[i] <= 2^31 - 1

"""
from typing import List
class MoveZeros:
    def moving_zeros(self,nums:List[int]) -> List[int]:
        """

        This function takes array intergers as input and moves all zeros to end and maintains relative order
        other elements.
        ------------------------------------------------------------------------------
        input : nums : List[int]
        return : nums : List[int]
        """
        temp=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[temp]=nums[i]
                temp+=1
        
        while temp <len(nums):
            nums[temp]=0
            temp+=1
        return nums

mz = MoveZeros()
print(mz.moving_zeros(list(map(int,input().split()))))
