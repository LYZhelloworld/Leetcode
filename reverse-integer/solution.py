class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if s[0] == '-':
            result = int('-' + s[1:][::-1])
        else:
            result = int(s[::-1])
        if result > 2 ** 31 - 1 or result < -(2 ** 31):
            result = 0
        return result
