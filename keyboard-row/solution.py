class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        row1 = 'qwertyuiopQWERTYUIOP'
        row2 = 'asdfghjklASDFGHJKL'
        row3 = 'zxcvbnmZXCVBNM'
        
        for word in words:
            if all([c in row1 for c in word]) or all([c in row2 for c in word]) or all([c in row3 for c in word]):
                res.append(word)
        
        return res
