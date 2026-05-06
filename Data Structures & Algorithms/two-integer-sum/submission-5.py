class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        freq = defaultdict() # {value: index}
        i = 0
        n = len(nums)
        while i<n:
            other = target - nums[i]
            if other in freq:
                return [freq[other], i]
            else:
                # add (nums[i], i) to the freq
                freq[nums[i]] = i
            i += 1
        return []