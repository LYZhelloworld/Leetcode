class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 1 + 3 + 5 + 7 + ... + (2*n-1) = n^2
        i = 1
        while num > 0:
            num -= i
            i += 2
        return 0 == num
