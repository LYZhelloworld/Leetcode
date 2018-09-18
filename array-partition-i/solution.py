class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum([i[1] if i[0] % 2 == 0 else 0 for i in enumerate(nums)])
