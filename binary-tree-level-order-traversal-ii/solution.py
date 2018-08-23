# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        queue = [root]

        while len(queue) > 0:
            tmp_queue = []
            group = []
            for item in queue:
                group.append(item.val)
                if item.left is not None:
                    tmp_queue.append(item.left)
                if item.right is not None:
                    tmp_queue.append(item.right)
            queue = tmp_queue
            result.append(group)
        result.reverse()
        return result
