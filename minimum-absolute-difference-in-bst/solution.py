# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        values = list(self.getValues(root))
        values.sort()
        pairs = zip([values[i] for i in range(0, len(values) - 1)], [values[i] for i in range(1, len(values))])
        diffs = (abs(i[0] - i[1]) for i in pairs)
        return min(diffs)
        
    def getValues(self, root):
        values = set()
        if root is None:
            return values
        
        values.add(root.val)
        values |= self.getValues(root.left)
        values |= self.getValues(root.right)
        return values
