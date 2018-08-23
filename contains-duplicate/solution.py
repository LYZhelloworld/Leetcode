class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        distinct_set = set()
        for n in nums:
            distinct_set.add(n)

        return not len(distinct_set) == len(nums)
