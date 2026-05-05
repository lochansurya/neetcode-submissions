class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        freq = Counter()
        for num in nums:
            if num in freq.keys():
                return True
            freq[num] += 1
        return False
        