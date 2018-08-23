import math

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return [self.nCr(rowIndex, i) for i in range(rowIndex + 1)]

    def nCr(self, n, r):
        f = math.factorial
        return f(n) // f(r) // f(n-r)
