class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''.join(i.lower() for i in s if i.isalnum())
        return (res[::] == res[::-1])