"""
<aside>
💡 **************Question 3**************

Given a string s consisting of words and spaces, return *the length of the **last** word in the string.*

A **word** is a maximal substring consisting of non-space characters only.

**Example 1:**

**Input:** s = "Hello World"

**Output:** 5

**Explanation:** The last word is "World" with length 5.

******************Solution:******************

One can break down the solution into two steps:

- First, we would try to locate the last word, starting from the end of the string. We iterate the string in reverse order, consuming the empty spaces. When we first come across a non-space character, we know that we are at the last character of the last word.
- Second, once we locate the last word. We count its length, starting from its last character. Again, we could use a loop here.
</aside>
"""

def length_last_word(sentence):
    p=len(sentence)-1

    while p>=0 and sentence[p]==' ':
        p-=1

    length =0
    while p>=0 and sentence[p]!=' ':
        p-=1
        length+=1
    return length 


print(length_last_word("hello world   "))