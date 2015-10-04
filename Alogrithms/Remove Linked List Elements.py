__author__ = 'responsible'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ans = iter = ListNode(None)
        ans.next = head
        while iter is not None and iter.next is not None:
            if iter.next.val == val:
                iter.next = iter.next.next
            else:
                iter = iter.next
        return ans.next