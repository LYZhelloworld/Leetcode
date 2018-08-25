import re

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return bool(re.compile('^0b1(00)*$').match(bin(num)))
