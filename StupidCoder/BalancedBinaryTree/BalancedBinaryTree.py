# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import TreeNode
import TreeParser


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        leftInfo = self.heightTreeAt(root.left)
        rightInfo = self.heightTreeAt(root.right)
        if rightInfo[1] == False or leftInfo[1] == False:
            return False
        elif abs(rightInfo[0] - leftInfo[0]) <= 1:
            return True
        else:
            return False


    def heightTreeAt(self, root):
        """
        :type root: TreeNode
        :rtype: [int, bool]: height of tree rooted at root, and if it is a balanced tree
        """

        if root is None:
            return 0, True

        if root.left is not None:
            leftInfo = self.heightTreeAt(root.left)
        else:
            leftInfo = [0, True]

        if root.right is not None:
            rightInfo = self.heightTreeAt(root.right)
        else:
            rightInfo = [0, True]

        if rightInfo[1] == False or leftInfo[1] == False:
            return 0, False
        elif abs(rightInfo[0] - leftInfo[0]) <= 1:
            return max(rightInfo[0], leftInfo[0]) + 1, True
        else:
            return 0, False


treeParser = TreeParser.TreeParser()
s = Solution()
root = treeParser.parseTree([3,9,20,None,None,15,7])
print(s.isBalanced(root))

