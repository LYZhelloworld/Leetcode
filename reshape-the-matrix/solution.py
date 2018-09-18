class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]): return nums
        
        def getNext(nums):
            for row in nums:
                for col in row:
                    yield col
        
        genNext = getNext(nums)
        return [[genNext.__next__() for col in range(c)] for row in range(r)]
