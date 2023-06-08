"""
<aside>
💡 ********************Question 2********************

Given two strings s and t, return true *if* t *is an anagram of* s*, and* false *otherwise*.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

**Input:** s = "anagram", t = "nagaram"

**Output:** true
**Complexity Analysis**

- Time complexity: *O*(*n*) because accessing the counter table is a constant time operation.
- Space complexity: *O*(1). Although we do use extra space, the space complexity is *O*(1) because the table's size stays constant no matter how large *n* is.
******************Solution:******************

</aside>
"""

def is_anagram(s,t):
    if len(s)!=len(t):
        return False 
    
    counter = [0]*26

    for i,j in zip(s,t):
        counter[ord(i)-ord('a')]+=1
        counter[ord(j)-ord('a')]-=1
    for count in counter:
        if count!=0:
            return False
    return True 
print(is_anagram('abcd', 'bdca'))