
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""



def isAnagram(s: str, t: str) -> bool:
    from collections import Counter
    s1 = Counter(s.lower())
    s2 = Counter(t.lower())

    return s1 == s2