class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        dict_s = {}
        dict_p = {}
        
        for c in p:
            if c in dict_p:
                dict_p[c] += 1
            else:
                dict_p[c] = 1
                
        for c in s[0:len(p)]:
            if c in dict_s:
                dict_s[c] += 1
            else:
                dict_s[c] = 1
                
        for i in range(0, len(s) - len(p) + 1):
            if i > 0:
                old_char = s[i - 1]
                new_char = s[i + len(p) - 1]
                
                dict_s[old_char] -= 1
                if dict_s[old_char] == 0:
                    del dict_s[old_char]
                    
                if new_char in dict_s:
                    dict_s[new_char] += 1
                else:
                    dict_s[new_char] = 1
            
            if dict_s == dict_p:
                result.append(i)
                
        return result
