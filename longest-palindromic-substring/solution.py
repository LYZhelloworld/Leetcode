class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''

        list_2core = self.find2core(s)
        list_3core = self.find3core(s)

        substrs = []
        for core in list_2core:
            substrs.append(self.check2core(s, core))
        for core in list_3core:
            substrs.append(self.check3core(s, core))

        if len(substrs) == 0:
            return s[0]
        return max(substrs, key = len)

    def find2core(self, s):
        # Find substrings like 'bb'
        # Keep the position of first character
        result = []
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                result.append(i)
        return result

    def find3core(self, s):
        # Find substrings like 'bab' or 'bbb'
        # Keep the position of second character
        result = []
        for i in range(len(s) - 2):
            if s[i] == s[i + 2]:
                result.append(i + 1)
        return result

    def check2core(self, s, pos):
        # Check if we can extend the substring while keeping it palindromic
        # Return substring
        substr = s[pos:pos + 2]
        i = 1
        while pos - i >= 0 and pos + i + 1 < len(s):
            if s[pos - i] == s[pos + i + 1]:
                substr = s[pos - i] + substr + s[pos + i + 1]
                i += 1
            else:
                break
        return substr

    def check3core(self, s, pos):
        # Check if we can extend the substring while keeping it palindromic
        # Return substring
        substr = s[pos - 1:pos + 2]
        i = 1
        while pos - i - 1 >= 0 and pos + i + 1 < len(s):
            if s[pos - i - 1] == s[pos + i + 1]:
                substr = s[pos - i - 1] + substr + s[pos + i + 1]
                i += 1
            else:
                break
        return substr
