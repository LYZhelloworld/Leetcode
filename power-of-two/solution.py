class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = bin(n)
        return binary == '0b1' + '0' * (len(binary) - 3)
