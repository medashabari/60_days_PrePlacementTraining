import heapq
def find_kth_smallestElement(nums,k):
    return heapq.nsmallest(k,nums)

find_kth_smallestElement([3,2,1,5,4,6],2)[-1]