class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = nums[:]
        for i, v in enumerate(self.sums):
            if i > 0:
                self.sums[i] = self.sums[i - 1] + v

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > 0:
            return self.sums[j] - self.sums[i - 1]
        else:
            return self.sums[j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
