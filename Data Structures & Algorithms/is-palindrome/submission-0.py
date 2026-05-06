class Solution:
    def remove_special_chars(self, 
        words: List[str])->List[str]:

        ans = [word for word in words if is_alnum(word)]
        return ans

    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join(ch.lower() for ch in s if ch.isalnum())
        return cleaned_s == cleaned_s[::-1]