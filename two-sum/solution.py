class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            try:
                j = nums.index(target - nums[i])
            except ValueError:
                continue
            if j == i:
                continue
            else:
                break
        return [i, j]
