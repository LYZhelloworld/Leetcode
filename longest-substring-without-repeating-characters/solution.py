class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_substr = 0
        tmp_str = ''
        for c in s:
            if c not in tmp_str:
                tmp_str += c
            else:
                length = len(tmp_str)
                if length > max_substr:
                    max_substr = length
                tmp_str = tmp_str[tmp_str.rfind(c) + 1:] + c

        length = len(tmp_str)
        if length > max_substr:
            max_substr = length

        return max_substr
