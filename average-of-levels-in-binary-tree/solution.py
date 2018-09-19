# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return []
        
        queue = [root]
        avgs = []
        while queue:
            newQueue = []
            values = []
            for node in queue:
                values.append(node.val)
                newQueue += ([node.left] if node.left is not None else []) + ([node.right] if node.right is not None else [])
            queue = newQueue
            avgs.append(sum(values) / len(values))
        return avgs
