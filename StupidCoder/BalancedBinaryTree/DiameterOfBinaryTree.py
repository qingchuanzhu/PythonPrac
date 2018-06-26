# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import TreeParser

class Solution:

    result = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.heightOfTreeAt(root)
        return self.result


    def heightOfTreeAt(self, node):
        if node == None:
            return -1
        if node.left is not None:
            left_height = self.heightOfTreeAt(node.left)
        else:
            left_height = -1
        if node.right is not None:
            right_height = self.heightOfTreeAt(node.right)
        else:
            right_height = -1

        pathLen = 2 + left_height + right_height
        if pathLen > self.result:
            self.result = pathLen

        return 1 + max(left_height, right_height)


treeParser = TreeParser.TreeParser()
s = Solution()
print(s.diameterOfBinaryTree(treeParser.parseTree([1,2,3,4,5])))
