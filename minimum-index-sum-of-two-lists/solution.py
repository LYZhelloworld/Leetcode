class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        common = set(list1) & set(list2)
        sums = {}
        for i in common:
            indexSum = list1.index(i) + list2.index(i)
            if indexSum not in sums:
                sums[indexSum] = []
            sums[indexSum].append(i)
        leastSum = min(sums.keys())
        return sums[leastSum]
