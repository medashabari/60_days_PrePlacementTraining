"""
Given a string s, find the length of the **longest substring** without repeating characters.

**Example 1:**

**Input:** s = "abcabcbb"

**Output:** 3

**Explanation:** The answer is "abc", with the length of 3.

"""

"""def lcs(s):
    res=[]
    word=''
    if len(s)==0:
        ""
    for i in s:
        if i not in word:
            word+=i
        else:
            res.append(word)
            word=""
    max_len = {i:len(i) for i in res}
    for key,val in max_len.items():
        if val==max(max_len.values()):
            return val
    return ""
    
print(lcs('aaabcbba'))"""

# sliding window
def lengthOfLongestSubstring(s):
    n = len(s)
    ans = 0
    map = {}  # current index of character
    # try to extend the range [i, j]
    i = 0
    for j in range(n):
        if s[j] in map:
            i = max(map[s[j]], i)
        ans = max(ans, j - i + 1)
        map[s[j]] = j + 1
    return ans
    
print(lengthOfLongestSubstring('abcabcaa'))