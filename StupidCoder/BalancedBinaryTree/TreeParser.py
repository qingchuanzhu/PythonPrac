import TreeNode


class TreeParser:
    def parseTree(self, tree):
        """
        :type tree: list[int]
        :rtype: root: TreeNode
        """

        return self.createTreeAt(0, tree)

    def createTreeAt(self, i, tree):
        if tree[i] is None:
            return None
        node = TreeNode.TreeNode(tree[i])
        leftChild_Index = 2 * i + 1
        rightChild_Index = 2 * i + 2
        if leftChild_Index <= len(tree) - 1:
            leftNode = self.createTreeAt(leftChild_Index, tree)
        else:
            leftNode = None

        if rightChild_Index <= len(tree) - 1:
            rightNode = self.createTreeAt(rightChild_Index, tree)
        else:
            rightNode = None

        node.left = leftNode
        node.right = rightNode

        return node
