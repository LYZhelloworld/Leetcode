class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        length_p = len(p)
        length_s = len(s)

        if length_p == 0:
            if length_s != 0:
                return False
            else:
                return True

        # remove duplicate patterns
        new_pattern = ''
        i = 0
        while i < length_p:
            new_pattern += p[i]
            if p[i] == '*' and i > 0 and p[i - 1] != '*':
                # /[a-z]*/
                while p[i + 1:].startswith(p[i - 1:i + 1]):
                    i += 2
                i += 1
                continue
            i += 1
        p = new_pattern
        length_p = len(p)

        ptr_p = 0
        ptr_s = 0

        flag_asterisk = False
        for ptr_p in range(length_p):
            if p[ptr_p] == '.':
                if ptr_p + 1 < length_p and p[ptr_p + 1] == '*':
                    # /.*/ any characters
                    flag_asterisk = True
                    if ptr_p + 2 < length_p:
                        for i in range(ptr_s, length_s + 1):
                            if self.isMatch(s[i:], p[ptr_p + 2:]):
                                return True
                        return False
                    else:
                        # end of pattern
                        # no matter what is left in the string (or nothing is left)
                        return True
                else:
                    # /./ one character
                    if ptr_s >= length_s:
                        # but there is no characters
                        return False
                    ptr_s += 1
            elif p[ptr_p] == '*':
                if not flag_asterisk:
                    # /*/ should not be used separately. fail
                    return False
                flag_asterisk = False
            else: # alphabets
                if ptr_p + 1 < length_p and p[ptr_p + 1] == '*':
                    # /[a-z]*/ repeat several times
                    flag_asterisk = True
                    for i in range(0, length_s - ptr_s + 1):
                        if s[ptr_s:].startswith(i * p[ptr_p]):
                            if self.isMatch(s[ptr_s + i:], p[ptr_p + 2:]):
                                return True
                    # no matches
                    return False
                else:
                    # just one alphabet
                    if ptr_s >= length_s or s[ptr_s] != p[ptr_p]:
                        return False
                    ptr_s += 1

        if ptr_s < length_s:
            # not matching entirely
            return False
        return True
