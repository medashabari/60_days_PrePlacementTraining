"""
<aside>
💡 ********************Question 5********************

**Balanced** strings are those that have an equal quantity of 'L' and 'R' characters.

Given a **balanced** string s, split it into some number of substrings such that:

- Each substring is balanced.

Return *the **maximum** number of balanced strings you can obtain.*

**Example 1:**

**Input:** s = "RLRRLLRLRL"

**Output:** 4

**Explanation:** s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

******************Solution:******************

Greedily split the string, and with the counting L +1

R -1, when the counter is reset to 0, we get one balanced string.

**************************************Complexity Analysis**************************************

Time Complexity : O(N)

Space Complexity : O(1)

</aside>
"""
def balance_string(s):
    cnt=0
    res=0
    for i in s:
        cnt+=1 if i=='L' else -1
        if cnt==0:
            res+=1
    return res 
print(balance_string("RLRRLLRLRL"))