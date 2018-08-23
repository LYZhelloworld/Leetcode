class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for row in range(numRows):
            tmp_row = []
            for i in range(row + 1):
                if i == 0 or i == row:
                    tmp_row.append(1)
                else:
                    tmp_row.append(result[row - 1][i] + result[row - 1][i - 1])
            result.append(tmp_row)
        return result
