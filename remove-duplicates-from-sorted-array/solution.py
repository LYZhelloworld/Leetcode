class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = None
        i = 0
        while i < len(nums):
            if last != nums[i]:
                last = nums[i]
                i += 1
            else:
                del nums[i]
        return len(nums)
