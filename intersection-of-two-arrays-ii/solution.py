class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return sum([[i] * min(nums1.count(i), nums2.count(i)) for i in (set(nums1) & set(nums2))], [])
