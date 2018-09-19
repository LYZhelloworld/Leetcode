class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        N = len(flowerbed)
        def getLeft(index):
            return True if index == 0 else flowerbed[index - 1] == 0
        def getRight(index):
            return True if index == N - 1 else flowerbed[index + 1] == 0
        def check(index):
            return flowerbed[index] == 0 and getLeft(index) and getRight(index)
        
        count = 0
        for index, value in enumerate(flowerbed):
            if check(index):
                flowerbed[index] = 1
                count += 1
                if count >= n: return True
        
        return count >= n
