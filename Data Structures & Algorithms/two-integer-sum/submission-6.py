class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict() # num: i
        for i, num in enumerate(nums):
            residue = target - num
            if residue in m.keys():
                return [m[residue], i]
            else:
                m[num] = m.get(num, 0) + i
        return [0, 0]