__author__ = 'responsible'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        ptr1_prev = ptr1_next = ptr2 = head
        while ptr2.next is not None and ptr2.next.next is not None:  # reverse the first half of the list
            ptr2 = ptr2.next.next
            ptr1_next = head.next
            head.next = ptr1_prev
            ptr1_prev = head
            head = ptr1_next
        if ptr2.next is None:  # if the case likes 1,2,3,2,1
            ptr2 = head.next
            head = ptr1_prev
        else:  # if the case likes 1,2,3,3,2,1
            if head.val != head.next.val: return False
            ptr2 = head.next.next
            head = ptr1_prev
        while ptr2 is not None:
            if head.val != ptr2.val:
                return False
            head = head.next
            ptr2 = ptr2.next
        return True