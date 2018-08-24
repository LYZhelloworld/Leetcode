class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 3:
            return []

        nums.sort()
        i = 0
        result = set()

        for i in range(0, length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            ptr1, ptr2 = i + 1, length - 1
            while ptr1 < ptr2:
                s = nums[ptr1] + nums[ptr2]
                if s == target:
                    result.add((nums[i], nums[ptr1], nums[ptr2]))
                    ptr1 += 1
                    while ptr1 < length - 1 and nums[ptr1] == nums[ptr1 - 1]:
                        ptr1 += 1
                    ptr2 -= 1
                    while ptr2 > 0 and nums[ptr2] == nums[ptr2 + 1]:
                        ptr2 -= 1
                elif s > target:
                    ptr2 -= 1
                    while ptr2 > 0 and nums[ptr2] == nums[ptr2 + 1]:
                        ptr2 -= 1
                else: # s < target
                    ptr1 += 1
                    while ptr1 < length - 1 and nums[ptr1] == nums[ptr1 - 1]:
                        ptr1 += 1

        # Remove duplicates
        #return [list(i) for i in result]
        return list(map(list, result))
