# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        counts = self.countItems(root)
        maximum = max(counts.values())
        res = []
        for k, v in counts.items():
            if v == maximum:
                res.append(k)
        return res
        
    def countItems(self, root):
        if root is None:
            return {}
        res = {}
        if root.left is not None:
            res = self.combineDicts(res, self.countItems(root.left))
        if root.right is not None:
            res = self.combineDicts(res, self.countItems(root.right))
        res = self.combineDicts(res, {root.val:1})
        return res
        
    def combineDicts(self, dict1, dict2):
        for k, v in dict2.items():
            if k in dict1:
                dict1[k] += v
            else:
                dict1[k] = v
        return dict1
