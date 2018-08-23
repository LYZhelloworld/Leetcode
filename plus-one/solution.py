class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = digits[:]
        result[-1] += 1

        result.reverse()
        for digit in range(len(result)):
            if result[digit] >= 10:
                result[digit] -= 10
                if digit == len(result) - 1:
                    result = result + [1]
                else:
                    result[digit + 1] += 1
        result.reverse()
        return result
