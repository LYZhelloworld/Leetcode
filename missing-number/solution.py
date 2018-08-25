class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i, v in enumerate(nums):
            if i > 0:
                if v != nums[i - 1] + 1:
                    return v - 1
            else:
                if v != 0:
                    return 0

        return nums[-1] + 1
