class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = 0
        exponent = 0
        s = s[::-1]

        while s != '':
            result += (letters.index(s[0]) + 1) * 26 ** exponent
            exponent += 1
            s = s[1:]

        return result
