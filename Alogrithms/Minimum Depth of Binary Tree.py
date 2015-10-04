__author__ = 'responsible'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root, depth = 1):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == root.right == None:
            return depth
        left = right = float("inf")
        if root.left is not None:
            left = self.minDepth(root.left, depth + 1)
        if root.right is not None:
            right = self.minDepth(root.right, depth + 1)
        return min(left, right)