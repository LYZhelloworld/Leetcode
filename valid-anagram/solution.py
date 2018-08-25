class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = {}
        dict_t = {}

        for c in s:
            if c not in dict_s:
                dict_s[c] = 1
            else:
                dict_s[c] += 1

        for c in t:
            if c not in dict_t:
                dict_t[c] = 1
            else:
                dict_t[c] += 1

        return dict_s == dict_t
