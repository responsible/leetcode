__author__ = 'responsible'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val =x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return head
        iter_odd = head
        head_even = iter_even = head.next
        while iter_even is not None and iter_even.next is not None:
            iter_odd.next = iter_even.next
            iter_odd = iter_odd.next
            iter_even.next = iter_odd.next
            iter_even = iter_even.next
        iter_odd.next = head_even
        return head