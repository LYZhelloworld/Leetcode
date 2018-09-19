class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        countNums = {}
        for n in nums:
            countNums[n] = countNums.get(n, 0) + 1
            if n + 1 in countNums:
                res = max(res, countNums[n] + countNums[n + 1])
            if n - 1 in countNums:
                res = max(res, countNums[n] + countNums[n - 1])
        return res
