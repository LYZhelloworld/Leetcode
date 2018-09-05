class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for i, c in enumerate(s):
            if c in count:
                count[c][0] += 1
            else:
                count[c] = [1, i]
                
        result = float('inf')
        for c, v in count.items():
            if v[0] == 1:
                if v[1] < result:
                    result = v[1]
        
        if result != float('inf'):
            return result
        else:
            return -1
