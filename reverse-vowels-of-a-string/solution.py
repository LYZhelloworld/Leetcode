class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ptr_l = 0
        ptr_r = len(s) - 1
        while ptr_l < ptr_r:
            if s[ptr_l] not in 'aeiouAEIOU':
                ptr_l += 1
                continue
            if s[ptr_r] not in 'aeiouAEIOU':
                ptr_r -= 1
                continue
            s = s[0:ptr_l] + s[ptr_r] + s[ptr_l + 1:ptr_r] + s[ptr_l] + s[ptr_r + 1:]
            ptr_l += 1
            ptr_r -= 1
        return s
