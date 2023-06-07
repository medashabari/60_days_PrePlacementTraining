"""
<aside>
💡 ********************Question 1********************

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

**Example 1:**

**Input:** jewels = "aA", stones = "aAAbbbb"

**Output:** 3

******************Solution:******************

**Intuition and Algorithm**

For each stone, check whether it matches any of the jewels. We can check efficiently with a *Hash Set*.

**Complexity Analysis**

- Time Complexity: *O*(*J*.length+*S*.length). The *O*(*J*.length) part comes from creating J. The *O*(*S*.length) part comes from searching S.
- Space Complexity: *O*(*J*.length).
</aside>
"""
def numJewelsInStones(J, S):
    Jset = set(J)
    ans = 0
    for s in S:
        if s in Jset:
            ans += 1
    return ans