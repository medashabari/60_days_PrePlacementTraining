import heapq

def find_kth_largestElement(nums,k):
    return heapq.nlargest(k,nums)

find_kth_largestElement([3,2,1,5,6,5],2)