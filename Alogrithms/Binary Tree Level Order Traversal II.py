__author__ = 'responsible'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        queue = deque()
        if root is not None:
            queue.append(root)
        while len(queue) != 0:
            ans.append(map(lambda x:x.val,list(queue)))
            for i in xrange(len(queue)):
                queue.extend(filter(lambda x:x is not None,[queue[0].left,queue[0].right]))
                queue.popleft()
        ans.reverse()
        return ans