"""
<aside>
💡 ********************Question 6********************

Given an input string s, reverse the order of the **words**.

A **word** is defined as a sequence of non-space characters. The **words** in s will be separated by at least one space.

Return *a string of the words in reverse order concatenated by a single space.*

**Note** that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

**Example 1:**

**Input:** s = "the sky is blue"

**Output:** "blue is sky the"

******************Solution:******************

**Approach 1: Built-in Split + Reverse**

**Complexity Analysis**

- Time complexity: O(*N*), where N is a number of characters in the input string.
- Space complexity: O(*N*), to store the result of split by spaces.
</aside>    
"""

def reverseWords(s):
    # remove leading and trailing spaces
    s = s.strip()
    # split by multiple spaces
    wordList = s.split()
    # reverse the list of words
    wordList.reverse()
    # join the words with a space separator
    return ' '.join(wordList)