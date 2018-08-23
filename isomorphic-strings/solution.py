class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = t[i]
            elif dic[s[i]] != t[i]:
                return False

        dic = {}
        for i in range(len(t)):
            if t[i] not in dic:
                dic[t[i]] = s[i]
            elif dic[t[i]] != s[i]:
                return False

        return True
