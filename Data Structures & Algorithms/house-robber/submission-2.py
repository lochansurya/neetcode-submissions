class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        table = nums[:]
        table[1] = max(table[0], table[1])
        i = 2
        while i < n:
            table[i] = max(nums[i] + table[i-2], table[i-1])
            i += 1
        return table[n-1]