class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        n = len(nums)
        l, h = 0, n - 1
        while l<=h:
            m = l + (h - l) // 2
            if nums[m]==target:
                ans = m
                break
            elif target < nums[m]:
                h = m -1
            else:
                l = m + 1
        return ans