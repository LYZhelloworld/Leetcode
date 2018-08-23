class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 0
        index2 = len(numbers) - 1

        while index1 < index2:
            difference = target - numbers[index2]
            if difference == numbers[index1]:
                return [index1 + 1, index2 + 1]

            if difference < numbers[index1]:
                index2 -= 1
            else:
                index1 += 1
