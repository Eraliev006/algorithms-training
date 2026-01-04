"""

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

"""



def isPalindrome(self, s: str) -> bool:
    s = s.lower()


    l, r = 0, len(s) - 1

    while l <= r:
        if not s[l].isalnum():
            l+=1
            continue
        if not s[r].isalnum():
            r-=1
            continue
    
        if s[l] != s[r]:
            return False

    return True