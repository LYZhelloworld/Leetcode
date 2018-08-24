class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ones =      ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')
        tens =      ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')
        hundreds =  ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')
        thousands = ('', 'M', 'MM', 'MMM')

        str_num = str(num)
        str_num = (4 - len(str_num)) * '0' + str_num # Convert it to 4 digits
        str_num = [int(i) for i in str_num]
        return thousands[str_num[0]] + hundreds[str_num[1]] + tens[str_num[2]] + ones[str_num[3]]
