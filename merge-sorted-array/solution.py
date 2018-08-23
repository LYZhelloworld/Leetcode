class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        current = 0

        for num in nums2:
            while current < m and nums1[current] <= num:
                current += 1
            self.insert_in_place(current, num, nums1)
            m += 1
        return

    def insert_in_place(self, index, obj, arr):
        for i in range(len(arr) - 2, index - 1, -1):
            arr[i + 1] = arr[i]
        arr[index] = obj
