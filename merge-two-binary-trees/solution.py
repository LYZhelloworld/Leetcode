class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        
        if t1 is None:
            t1 = TreeNode(0)
        if t2 is None:
            t2 = TreeNode(0)
        t1.val = t1.val + t2.val
        
        if not (t1.left is None and t2.left is None):
            if t1.left is None:
                t1.left = TreeNode(0)
            if t2.left is None:
                t2.left = TreeNode(0)
            self.mergeTrees(t1.left, t2.left)
            
        if not (t1.right is None and t2.right is None):
            if t1.right is None:
                t1.right = TreeNode(0)
            if t2.right is None:
                t2.right = TreeNode(0)
            self.mergeTrees(t1.right, t2.right)
            
        return t1
