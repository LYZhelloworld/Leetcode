"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        def calc(quadTree1, quadTree2):
            if quadTree1.isLeaf:
                return Node(True, True, None, None, None, None) if quadTree1.val else quadTree2
            elif quadTree2.isLeaf:
                return Node(True, True, None, None, None, None) if quadTree2.val else quadTree1
            else:
                res = Node(False,
                           False,
                           calc(quadTree1.topLeft, quadTree2.topLeft),
                           calc(quadTree1.topRight, quadTree2.topRight),
                           calc(quadTree1.bottomLeft, quadTree2.bottomLeft),
                           calc(quadTree1.bottomRight, quadTree2.bottomRight))
                if res.topLeft.isLeaf and res.topRight.isLeaf and res.bottomLeft.isLeaf and res.bottomRight.isLeaf:
                    if res.topLeft.val and res.topRight.val and res.bottomLeft.val and res.bottomRight.val:
                        res.isLeaf = True
                        res.val = True
                return res
            
        return calc(quadTree1, quadTree2)
