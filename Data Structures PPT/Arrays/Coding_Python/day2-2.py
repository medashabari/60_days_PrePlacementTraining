"""
Question 2
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping
intervals, and return an array of the non-overlapping intervals that cover all the
intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Solution:
Java: https://pastebin.com/fSmRxP9M
Python: https://pastebin.com/DsTCaT1w
Javascript: https://pastebin.com/jEDe46tn
TC : O(nlogn)
SC : O (log n)
"""
"""
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
"""
from typing import List
def merge_intervals(arr:List[List[int]]):
    result=[arr[0]]
    arr.sort(key=lambda x:x[0])

    for i in range(1,len(arr)):
        if result[-1][1] > arr[i][0]:
            result[-1][1] = arr[i][1]
        else:
            result.append(arr[i])
    return result

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))