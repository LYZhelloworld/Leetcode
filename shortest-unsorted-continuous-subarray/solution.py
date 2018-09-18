class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newNums = nums[:]
        newNums.sort()
        
        start = end = None
        for i in range(0, len(newNums)):
            if nums[i] != newNums[i]:
                start = i
                break
        if start is None:
            return 0
        
        for i in range(len(newNums) - 1, -1, -1):
            if nums[i] != newNums[i]:
                end = i
                break
        return end - start + 1
