class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last_non_zero_index = 0

        for i, v in enumerate(nums):
            if v:
                nums[last_non_zero_index] = v
                last_non_zero_index += 1
        for i in range(last_non_zero_index, len(nums)):
            nums[i] = 0
