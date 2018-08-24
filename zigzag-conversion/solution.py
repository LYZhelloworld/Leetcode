class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows, cols = self.calcRowsCols(len(s), numRows)

        grids = [['' for j in range(cols)] for i in range(rows)]
        row = 0
        col = 0
        turn = False
        for c in s:
            grids[row][col] = c
            if not turn:
                row += 1
                if row == numRows:
                    if numRows > 2:
                        turn = True
                        row -= 2
                        col += 1
                    else:
                        row = 0
                        col += 1
            else:
                row -= 1
                col += 1
                if row == 0:
                    turn = False

        return self.outputGrids(grids)

    def calcRowsCols(self, length, numRows):
        rows = numRows
        d = numRows + max(numRows - 2, 0)
        q = length // d
        r = length % d
        cols = q * (1 + max(numRows - 2, 0)) + (0 if r == 0 else 1 if 0 < r <= numRows else 1 + r - numRows)
        return rows, cols

    def outputGrids(self, grids):
        return ''.join([''.join(grids[row]) for row in range(len(grids))])
