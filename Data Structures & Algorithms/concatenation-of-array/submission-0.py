class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        item = lambda nums: (x for x in nums)
        ans += list(item(nums))
        return ans
