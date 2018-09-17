class Solution():
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0 or len(nums) == 0:
            return 0
        
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        distinctNums = counts.keys()
        
        res = 0
        if k == 0:
            for num in distinctNums:
                if counts[num] > 1:
                    res += 1
        else:
            for num in distinctNums:
                if num + k in counts:
                    res += 1
        return res
