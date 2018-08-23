class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''

        while n > 0:
            quotient = (n - 1) // 26
            remainder = (n - 1) % 26
            result = letters[remainder] + result
            n = quotient

        return result
