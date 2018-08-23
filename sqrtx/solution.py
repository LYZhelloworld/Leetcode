class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 1
        right = x
        mid = (right - left) // 2 + left

        while right - left > 1:
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            if mid ** 2 > x:
                right = mid
            else:
                left = mid
            mid = (right - left) // 2 + left
        return mid
