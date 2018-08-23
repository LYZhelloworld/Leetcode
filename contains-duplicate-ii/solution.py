class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_occur = {}

        for i in range(len(nums)):
            if nums[i] not in last_occur:
                last_occur[nums[i]] = i
            else:
                if i - last_occur[nums[i]] <= k:
                    return True
                else:
                    last_occur[nums[i]] = i

        return False
