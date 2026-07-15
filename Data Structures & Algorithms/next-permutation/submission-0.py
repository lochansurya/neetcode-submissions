class Solution:
    def reverse(self, arr: List[int], start: int, end: int):
        low, high = start, end
        while low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1] :
            i -= 1
        
        if i >= 0 :
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left = i + 1
        right = n - 1
        self.reverse(nums, left, right)