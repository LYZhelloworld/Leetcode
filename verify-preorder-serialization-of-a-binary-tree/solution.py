class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        values = preorder.split(',')
        root = True
        pos = [] # True = left, False = right
        for v in values:
            if v != '#':
                if len(pos) == 0 and not root:
                    # Error: multiple roots
                    return False
                # Next layer
                pos += [True]
                root = False
            else:
                if len(pos) == 0:
                    if not root:
                        # Error
                        return False
                    else:
                        # Empty tree
                        root = False
                while len(pos) > 0:
                    if pos[-1]: # Left
                        pos[-1] = False
                        break
                    else: # Right
                        pos = pos[:-1]
        if len(pos) == 0:
            return True
        else:
            return False
