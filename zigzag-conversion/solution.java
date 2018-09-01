import java.util.*;

class Solution {
    public String convert(String s, int numRows) {
        int[] result = calcRowsCols(s.length(), numRows);
        int rows = result[0], cols = result[1];
        
        char[][] grids = new char[rows][cols];
        int row = 0, col = 0;
        boolean turn = false;
        
        for(char c : s.toCharArray()) {
            grids[row][col] = c;
            if(!turn) {
                ++row;
                if(row == numRows) {
                    if(numRows > 2) {
                        turn = true;
                        row -= 2;
                        ++col;
                    } else {
                        row = 0;
                        ++col;
                    }
                }
            } else {
                --row;
                ++col;
                if(0 == row) {
                    turn = false;
                }
            }
        }
        
        return outputGrids(grids);
    }
    
    private int[] calcRowsCols(int length, int numRows) {
        int rows = numRows;
        int d = numRows + Math.max(numRows - 2, 0);
        int q = length / d;
        int r = length % d;
        int cols = q * (1 + Math.max(numRows - 2, 0)) + (0 == r ? 0 : r > 0 && r <= numRows ? 1 : 1 + r - numRows);
        return new int[] {rows, cols};
    }
    
    private String outputGrids(char[][] grids) {
        String result = "";
        for(int row = 0; row < grids.length; ++row) {
            for(int col = 0; col < grids[0].length; ++col) {
                result += grids[row][col] != '\0' ? grids[row][col] : "";
            }
        }
        return result;
    }
}
