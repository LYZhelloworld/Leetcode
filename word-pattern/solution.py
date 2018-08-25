class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ptow = {}
        wtop = {}
        words = str.split()
        if len(words) != len(pattern):
            return False

        for p, w in zip(pattern, words):
            if p not in ptow:
                ptow[p] = w
            elif ptow[p] != w:
                return False

            if w not in wtop:
                wtop[w] = p
            elif wtop[w] != p:
                return False

        return True
