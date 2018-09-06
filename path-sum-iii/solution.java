/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int pathSum(TreeNode root, int sum) { // root is root
        if(root == null) return 0;
        int count = 0;
        if(root.val == sum)
            count++;
        if(root.left != null) {
            count += find(root.left, sum - root.val);
            count += pathSum(root.left, sum);
        }
        if(root.right != null) {
            count += find(root.right, sum - root.val);
            count += pathSum(root.right, sum);
        }
        return count;
    }
    
    private int find(TreeNode root, int current_sum) { // root is not root
        int count = 0;
        if(root.val == current_sum) 
            count++;
        if(root.left != null) {
            count += find(root.left, current_sum - root.val);
        }
        if(root.right != null) {
            count += find(root.right, current_sum - root.val);
        }
        return count;
    }
}
