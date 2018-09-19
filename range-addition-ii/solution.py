class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if len(ops) == 0: return m * n
        minX = minY = float('inf')
        for op in ops:
            minX = min(minX, op[0])
            minY = min(minY, op[1])
        return minX * minY
