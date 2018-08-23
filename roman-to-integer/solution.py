class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones =      (None, 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')
        tens =      (None, 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')
        hundreds =  (None, 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')
        thousands = (None, 'M', 'MM', 'MMM')

        result = 0
        comparison = (3, 2, 4, 9, 1, 8, 7, 6, 5)
        comparison_thousands = (3, 2, 1)
        num = s
        for token in comparison_thousands:
            if(num.startswith(thousands[token])):
                result += 1000 * token
                num = num[len(thousands[token]):]
                break
        for token in comparison:
            if(num.startswith(hundreds[token])):
                result += 100 * token
                num = num[len(hundreds[token]):]
                break
        for token in comparison:
            if(num.startswith(tens[token])):
                result += 10 * token
                num = num[len(tens[token]):]
                break
        for token in comparison:
            if(num.startswith(ones[token])):
                result += token
                num = num[len(ones[token]):]
                break

        return result
