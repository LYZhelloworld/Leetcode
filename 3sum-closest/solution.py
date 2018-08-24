class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length < 3:
            return 0

        nums.sort()
        i = 0
        closest_target = float('inf')

        for i in range(0, length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            t = target - nums[i]
            ptr1, ptr2 = i + 1, length - 1
            while ptr1 < ptr2:
                s = nums[ptr1] + nums[ptr2]
                if s == t:
                    # exactly
                    return target
                elif s > t:
                    if abs(nums[i] + s - target) < abs(closest_target - target):
                        closest_target = nums[i] + s
                    ptr2 -= 1
                    while ptr2 > 0 and nums[ptr2] == nums[ptr2 + 1]:
                        ptr2 -= 1
                else: # s < t
                    if abs(nums[i] + s - target) < abs(closest_target - target):
                        closest_target = nums[i] + s
                    ptr1 += 1
                    while ptr1 < length - 1 and nums[ptr1] == nums[ptr1 - 1]:
                        ptr1 += 1


        return closest_target
