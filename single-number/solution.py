class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        occurrence = []
        for n in nums:
            if n not in occurrence:
                occurrence.append(n)
            else:
                occurrence.remove(n)
        return occurrence[0]
        '''
        result = 0
        for n in nums:
            result ^= n
        return result
