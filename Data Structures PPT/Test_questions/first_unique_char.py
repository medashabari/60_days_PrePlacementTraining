"""
First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
a. 1 <= s.length <= 10^5
b. s consists of only lowercase English letters.
"""

class UniqueCharacter:
    def uniqueCharter(self,s:str) -> int:
        """
        This fuction takes string a input and returns index of first unique element
        if no unique element founds return -1

        input : s:string
        return : index:int

        """
        freq_counter = {} # stores frequency of each element
        index={} # stores first index each element
        for i in range(len(s)):
            if s[i] not in freq_counter:
                freq_counter[s[i]]=1
                index[s[i]] = i
            else:
                freq_counter[s[i]]+=1

        for key,value in freq_counter.items():
            if value==1:
                return index[key]
        return -1


uc = UniqueCharacter()
print(uc.uniqueCharter(input()))
