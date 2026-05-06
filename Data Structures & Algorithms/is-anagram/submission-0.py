class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        freq_s = Counter(s)
        freq_t = Counter(t)
        return freq_s==freq_t
