class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sums = []
        for n in nums:
            if len(sums) == 0:
                sums.append(n)
            else:
                sums.append(sums[-1] + n)
        
        maxAvg = sums[k - 1]
        for i in range(k, len(sums)):
            maxAvg = max(maxAvg, sums[i] - sums[i - k])
        return maxAvg / k
