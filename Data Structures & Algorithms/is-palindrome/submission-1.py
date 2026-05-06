class Solution:
    def remove_non_alnum(self,
        s: str)-> str:
        ans = ''.join(ch.lower() for ch in s if ch.isalnum())
        return ans
    def isPalindrome(self, s: str) -> bool:
        s = self.remove_non_alnum(s)
        return s==s[::-1]