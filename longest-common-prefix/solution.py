class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        prefix = strs[0]
        while not all([s.startswith(prefix) for s in strs]):
            prefix = prefix[:-1]
            if len(prefix) == 0:
                break
        return prefix
