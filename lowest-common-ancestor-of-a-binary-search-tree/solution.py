# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root

        if p.val > q.val:
            p, q = q, p

        while not p.val <= root.val <= q.val:
            if p.val <= root.val and q.val <= root.val:
                root = root.left
            else:
                root = root.right

        return root
