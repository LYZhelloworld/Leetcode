class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        count = 0
        current = None

        if n == 1:
            return '1'

        s = self.countAndSay(n - 1)
        for c in s:
            if current is None:
                current = c
                count += 1
            elif current != c:
                result += str(count) + current
                count = 1
                current = c
            else:
                count += 1
        result += str(count) + current
        return result
