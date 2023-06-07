"""
<aside>
💡 ********************Question 3********************

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

**Example 1:**

**Input:** s = "A man, a plan, a canal: Panama"

**Output:** true

**Explanation:** "amanaplanacanalpanama" is a palindrome.

******************Solution:******************

Since the input string contains characters that we need to ignore in our palindromic check, it becomes tedious to figure out the real middle point of our palindromic input.

So, if we start traversing inwards, from both ends of the input string, we can expect to *see* the same characters, in the same order.

The resulting algorithm is simple:

- Set two pointers, one at each end of the input string
- If the input is palindromic, both the pointers should point to equivalent characters, *at all times*. [1](https://leetcode.com/problems/valid-palindrome/editorial/#user-content-fn-note-1)
    - If this condition is not met at any point of time, we break and return early. [2](https://leetcode.com/problems/valid-palindrome/editorial/#user-content-fn-note-2)
- We can simply ignore non-alphanumeric characters by continuing to traverse further.
- Continue traversing inwards until the pointers meet in the middle.

**Complexity Analysis**

- Time complexity : *O*(*n*), in length *n* of the string. We traverse over each character at-most once, until the two pointers meet in the middle, or when we break and return early.
- Space complexity : *O*(1). No extra space required, at all.
</aside>
"""
"""
def phrase_palindrome(s):
    res=''
    for i in s.lower():
        if i!=' ' and i.isalnum():
            res+=i
    return res == res[::-1]
print(phrase_palindrome("A man, a plan, a canal: Panama"))"""

def phrase_palindrome(s):
    i=0
    j=len(s)-1
    
    while i<j:
        while i<j and not s[i].isalnum():
            i+=1
        
        while i<j and not s[j].isalnum():
            j-=1
        
        if s[i].lower()!=s[j].lower():
            return False 
        i+=1
        j-=1
    return True 
print(phrase_palindrome("A man, a plan, a canal: Panama"))