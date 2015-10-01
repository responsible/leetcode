__author__ = 'responsible'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        iter = head
        while iter != None:
            while iter.next !=None and iter.next.val == iter.val:
                iter.next = iter.next.next
            else:
                iter = iter.next
        return head
