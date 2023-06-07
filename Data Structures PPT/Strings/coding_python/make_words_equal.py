"""
<aside>
💡 ********************Question 4********************

You are given an array of strings words (**0-indexed**).

In one operation, pick two **distinct** indices i and j, where words[i] is a non-empty string, and move **any** character from words[i] to **any** position in words[j].

Return true *if you can make **every** string in* words ***equal** using **any** number of operations*, *and* false *otherwise*.

**Example 1:**

**Input:** words = ["abc","aabc","bc"]

**Output:** true

**Explanation:** Move the first 'a' in words[1] to the front of words[2],

to make words[1] = "abc" and words[2] = "abc".

All the strings are now equal to "abc", so return true.

****************Solution:****************

**************************************Complexity Analysis**************************************

Time Complexity: O(N)

Space Complexity : O(1)

</aside>
"""

"""def make_equal(s):
    freq_counter={}

    new=''
    for i in s:
        new+=i 
    
    for i in new:
        freq_counter[i] = freq_counter.get(i,0)+1 
    
    for val in freq_counter.values():
        if val%len(s)!=0:
            return False 
    
    return True 

print(make_equal(['aab','ab','aaab']))"""


def make_equal(s):
    freq_counter = [0]*26

    for word in s:
        for i in word:
            freq_counter[ord(i)-ord('a')]+=1
    for i in freq_counter:
        if i % len(s)!=0:
            return False 
    return True

print(make_equal(['aab','ab','aaab']))