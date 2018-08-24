class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = 0
        negative = False
        first_sign = True
        first_space = True
        digits = '0123456789'
        for c in str:
            if first_space and c == ' ':
                continue
            elif first_sign and c == '-':
                negative = True
                first_sign = False
                first_space = False
            elif first_sign and c == '+':
                negative = False
                first_sign = False
                first_space = False
            elif c in digits:
                first_sign = False
                first_space = False
                result = result * 10 + digits.find(c)
            else:
                break
        result = -result if negative else result
        result = max(min(result, 2 ** 31 - 1), -2 ** 31)
        return result
