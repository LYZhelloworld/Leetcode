class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = ''
        for c in s:
            if c in ('(', '{', '['):
                stack += c
            elif c == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                stack = stack[:-1]
            elif c == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                stack = stack[:-1]
            elif c == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                stack = stack[:-1]
            # Ignore other characters
        if len(stack) != 0:
            return False
        return True
