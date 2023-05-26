from typing import List
def threeSum(nums:List[int]) -> List[List[int]]:
    # sort the array
    nums.sort()
    res=[]
    for i in range(len(nums)):
        if nums[i]>0:
            break
        if i==0 or nums[i-1]!=nums[i]:
            twoSum(nums,i,res)
    return res
def twoSum(nums,i,res):
    left_ptr = i+1
    right_ptr=len(nums)-1
    while left_ptr < right_ptr:
        sum=nums[left_ptr]+nums[right_ptr]+nums[i]
        if sum<0:
            left_ptr+=1
        elif sum>0:
            right_ptr-=1
        else:
            res.append([nums[left_ptr],nums[right_ptr],nums[i]])
            left_ptr+=1
            right_ptr-=1
            while left_ptr < right_ptr and nums[left_ptr]==nums[left_ptr-1]:
                left_ptr+=1

        

print(threeSum([-1,0,1,2,-4,-4]))

