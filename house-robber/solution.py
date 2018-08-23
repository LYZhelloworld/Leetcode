class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        dp = [[0, 0] for i in nums] # dp[i][0] for not robbing the house, dp[i][1] for robbing.
        dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) # Ignore this house. Choose the max result of previous one.
            dp[i][1] = dp[i - 1][0] + nums[i] # Rob this house. Must not rob the previous one, and +amount of this one.

        return max(dp[-1][0], dp[-1][1])
