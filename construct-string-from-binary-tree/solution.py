class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None: return ''
        res = str(t.val)
        if t.left is not None:
            res += '(' + self.tree2str(t.left) + ')'
        else:
            if t.right is not None:
                res += '()'
        if t.right is not None:
            res += '(' + self.tree2str(t.right) + ')'
        return res
