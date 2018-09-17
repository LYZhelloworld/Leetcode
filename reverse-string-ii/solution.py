class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        newStr = ''
        isReverse = True
        for i in range(0, len(s), k):
            if isReverse:
                newStr += s[i:i + k][::-1]
                isReverse = False
            else:
                newStr += s[i:i + k]
                isReverse = True
        return newStr
