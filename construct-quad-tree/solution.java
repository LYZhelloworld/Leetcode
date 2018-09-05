/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    public Node() {}

    public Node(boolean _val,boolean _isLeaf,Node _topLeft,Node _topRight,Node _bottomLeft,Node _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/
class Solution {
    public Node construct(int[][] grid) {
        return getNodes(grid, 0, grid.length, 0, grid[0].length);
    }
    
    private Node getNodes(int[][] grid, int x1, int x2, int y1, int y2) {
        if(x2 - x1 == 1 && y2 - y1 == 1) {
            // Leaf
            return new Node(grid[x1][y1] == 1, true, null, null, null, null);
        }
        
        int xMid = (x2 - x1) / 2 + x1;
        int yMid = (y2 - y1) / 2 + y1;
        Node topLeft = getNodes(grid, x1, xMid, y1, yMid);
        Node topRight = getNodes(grid, x1, xMid, yMid, y2);
        Node bottomLeft = getNodes(grid, xMid, x2, y1, yMid);
        Node bottomRight = getNodes(grid, xMid, x2, yMid, y2);
        
        if(topLeft.isLeaf && topRight.isLeaf && bottomLeft.isLeaf && bottomRight.isLeaf) {
            if(topLeft.val == topRight.val && topRight.val == bottomLeft.val && bottomLeft.val == bottomRight.val) {
                // Leaf
                return new Node(topLeft.val, true, null, null, null, null);
            }
        }
        return new Node(false, false, topLeft, topRight, bottomLeft, bottomRight);
    }
}
