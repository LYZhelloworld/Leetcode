class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_current = nums[0]
        max_global = nums[0]
        for n in nums[1:]:
            max_current = max(n, n + max_current)
            max_global = max(max_current, max_global)
        return max_global
