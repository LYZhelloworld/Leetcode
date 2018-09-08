class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        medals = ('Gold Medal', 'Silver Medal', 'Bronze Medal')
        
        mapped = list(zip(nums, range(len(nums))))
        mapped.sort(key=lambda x: x[0], reverse=True)
        for i, v in enumerate(mapped):
            nums[v[1]] = medals[i] if i in range(3) else str(i + 1)
        return nums
