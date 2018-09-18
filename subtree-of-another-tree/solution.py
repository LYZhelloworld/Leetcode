class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def compare(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            return a.val == b.val and compare(a.left, b.left) and compare(a.right, b.right)
        
        if s is None:
            return False
        
        if s.val == t.val:
            # Same value. Compare sub-nodes
            if compare(s.left, t.left) and compare(s.right, t.right):
                return True
        
        # Different value, or sub-nodes are different
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
