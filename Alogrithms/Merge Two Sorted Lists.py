__author__ = 'responsible'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = iter = ListNode(None)
        while l1 is not None and l2 is not None:
            iter.next = ListNode(None)
            iter = iter.next
            if l1.val < l2.val:
                iter.val = l1.val
                l1 = l1.next
            else:
                iter.val = l2.val
                l2 = l2.next
        if l1 is None:
            iter.next = l2
        else:
            iter.next = l1
        return ans.next