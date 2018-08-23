class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Remove continuous duplicates
        i = 1
        while i < len(prices):
            if prices[i] == prices[i - 1]:
                del prices[i]
                continue
            i += 1

        length = len(prices)
        if length == 1:
            return 0

        profit = 0
        minimum = float('inf')

        for i in range(length):
            if self.isMinimum(prices, i):
                minimum = prices[i]
                continue

            if self.isMaximum(prices, i):
                if minimum != float('inf'):
                    profit += prices[i] - minimum
                    minimum = float('inf')

        return profit

    def isMaximum(self, prices, i):
        if i == 0:
            return prices[i] > prices[i + 1]
        elif i == len(prices) - 1:
            return prices[i - 1] < prices[i]
        else:
            return prices[i - 1] < prices[i] > prices[i + 1]

    def isMinimum(self, prices, i):
        if i == 0:
            return prices[i] < prices[i + 1]
        elif i == len(prices) - 1:
            return prices[i - 1] > prices[i]
        else:
            return prices[i - 1] > prices[i] < prices[i + 1]
