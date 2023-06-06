"""
<aside>
💡 ********************Question 4********************

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

**Example 1:**

**Input:** strs = ["flower","flow","flight"]

**Output:** "fl"

"""

def Lcp(strs):
    if len(strs)==0:
        return ""
    prefix=strs[0]
    for i in range(1,len(strs)):
        while strs[i].find(prefix)!=0:
            prefix = prefix[:-1]
            if len(prefix)==0:
                return ""
    return prefix

print(Lcp(["flower","flow","flight"]))