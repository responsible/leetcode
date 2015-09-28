__author__ = 'responsible'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum, curSum=0):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        if root.left == root.right == None:
            return sum == curSum + root.val
        return self.hasPathSum(root.left, sum, curSum + root.val) or self.hasPathSum(root.right, sum, curSum + root.val)