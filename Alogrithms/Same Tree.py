__author__ = 'responsible'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return p == q == None or (None not in (p, q) and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))