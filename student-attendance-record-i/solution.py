class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if 'LLL' in s:
            return False
        countA = 0
        for c in s:
            if c == 'A':
                countA += 1
                if countA > 1:
                    return False
        return True
