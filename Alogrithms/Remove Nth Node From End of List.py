__author__ = 'responsible'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ans = leftPtr = rightPtr = ListNode(None)
        leftPtr.next = head
        for i in xrange(n):
            rightPtr = rightPtr.next
        while rightPtr.next is not None:
            leftPtr = leftPtr.next
            rightPtr = rightPtr.next
        leftPtr.next = leftPtr.next.next
        return ans.next