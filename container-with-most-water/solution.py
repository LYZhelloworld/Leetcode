class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0

        start = 0
        end = len(height) - 1
        max_area = 0

        while end - start > 0:
            area = (end - start) * min(height[start], height[end])
            max_area = max(max_area, area)
            if height[end] < height[start]:
                end -= 1
            else:
                start += 1

        return max_area
