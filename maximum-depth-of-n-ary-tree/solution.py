"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def __init__(self):
        self.depth = 0
    
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        
        def getMaxDepth(root, current):
            self.depth = max(self.depth, current)
            for child in root.children:
                getMaxDepth(child, current + 1)
        
        getMaxDepth(root, 1)
        return self.depth
