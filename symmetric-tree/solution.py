# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root.left, root.right) if root is not None else True

    def isMirror(self, left, right):
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left) if left is not None and right is not None else left is None and right is None
