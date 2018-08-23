import math

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occurrences = {}
        target = math.ceil(len(nums) / 2)

        for n in nums:
            if n not in occurrences:
                occurrences[n] = 1
            else:
                occurrences[n] += 1

        for n in occurrences:
            if occurrences[n] >= target:
                return n
