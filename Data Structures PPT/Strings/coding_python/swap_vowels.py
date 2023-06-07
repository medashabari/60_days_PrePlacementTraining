"""
<aside>
💡 ********************Question 6********************

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

**Example 1:**

**Input:** s = "hello"

**Output:** "holle"

******************Solution:******************

**Algorithm**

1. Initialize the left pointer start to 0, and the right pointer end to s.size() - 1.
2. Keep iterating until the left pointer catches up with the right pointer:
    1. Keep incrementing the left pointer start until it's pointing to a vowel character.
    2. Keep decrementing the right pointer end until it's pointing to a vowel character.
    3. Swap the characters at the start and end.
    4. Increment the start pointer and decrement the end pointer.
3. Return the string s.

**Complexity Analysis**

Here, *N* is the length of the string s.

- Time complexity: *O*(*N*)
    
    It might be tempting to say that there are two nested loops and hence the complexity would be
    
- *O*(*N^2*). However, if we observe closely the pointers start and end will only traverse the index once. Each element of the string s will be iterated only once either by the left or right pointer and not both. We swap characters when both pointers point to vowels which are *O*(1) operation. Hence the total time complexity will be *O*(*N*).
    
    Note that in Java we need to convert the string to a char array as strings are immutable and hence it would take *O*(*N*) time.
    
- Space complexity: *O*(*N*)
    
    In C++ we only need an extra temporary variable to perform the swap and hence the space complexity is *O*(1). However, in Java, we need to convert the string to a char array that would take *O*(*N*) space, and therefore the space complexity for Java would be *O*(*N*).
    
</aside>
"""


class Swapping_Vowels:

    def swap(self,s_list,i,j):
        s_list[i],s_list[j] = s_list[j],s_list[i]

    def is_vowel(self,letter):
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        return letter in vowels

    def reverse_vowels(self,s):
        left = 0
        right = len(s)-1
        s_list = list(s)
        while left < right:

            while left < (len(s)) and not self.is_vowel(s_list[left]):
                left+=1
            
            while right >=0 and not self.is_vowel(s_list[right]):
                right-=1
            
            if left < right:
                self.swap(s_list, left, right)
                left+=1
                right-=1
        return "".join(s_list)


sv = Swapping_Vowels()
print(sv.reverse_vowels("hello"))