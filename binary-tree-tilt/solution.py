# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def calc(root):
            if not root: return 0
            left = calc(root.left)
            right = calc(root.right)
            nonlocal tilt
            tilt += abs(left - right)
            return left + right + root.val
        
        tilt = 0
        calc(root)
        return tilt
