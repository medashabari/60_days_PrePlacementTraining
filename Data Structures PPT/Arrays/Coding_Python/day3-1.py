"""
Question 1
Implement pow(x, n), which calculates x raised to the power n (i.e., x
n
).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000
Solution:
Java: https://pastebin.com/ZXPjuVa4
Python: https://pastebin.com/4kvtricN
Javascript: https://pastebin.com/4vc1NVtb
TC : O(log n)
SC : O(1)
"""

class Solution:
    def pow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        return x * self.pow(x * x, n // 2) if n % 2 else self.pow(x * x, n // 2)
 
obj = Solution()
print(obj.pow(2, 10))