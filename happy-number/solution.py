class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        occurrences = []

        while n not in occurrences and n != 1:
            occurrences.append(n)
            n = self.next(n)

        if n == 1:
            return True
        else:
            return False

    def next(self, n):
        return sum(int(i) * int(i) for i in str(n))
