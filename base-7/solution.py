class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        negative = num < 0
        num = abs(num)
        
        res = ''
        while num > 0:
            q = num // 7
            r = num % 7
            res = str(r) + res
            num = q
            print(res)
        
        if res == '':
            res = '0'
        res = ('-' if negative else '') + res
        return res
