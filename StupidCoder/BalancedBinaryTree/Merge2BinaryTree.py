
import TreeParser

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        elif t1 is None:
            return t2
        elif t2 is None:
            return t1

        t1.val = t1.val + t2.val

        left = self.mergeTrees(t1.left, t2.left)
        right = self.mergeTrees(t1.right, t2.right)
        t1.left = left
        t1.right = right
        return t1

treeParser = TreeParser.TreeParser()
t1 = treeParser.parseTree([1,3,2,5])
t2 = treeParser.parseTree([2,1,3,None,4,None,7])
s = Solution()
s.mergeTrees(t1, t2)