__author__ = 'responsible'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root,depth=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return depth
        return max(self.maxDepth(root.left,depth+1),self.maxDepth(root.right,depth+1))