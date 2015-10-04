__author__ = 'responsible'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = next = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev