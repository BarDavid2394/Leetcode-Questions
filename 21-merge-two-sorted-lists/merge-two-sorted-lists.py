# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        current = dummy
        if not l1 :
            return l2
        if not l2 :
            return l1
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        return dummy.next

                

























        # dummy_head = ListNode()
        # current = dummy_head
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         current.next = l1
        #         l1 = l1.next
        #     else:
        #         current.next = l2
        #         l2 = l2.next
        #     current = current.next
        # current.next = l2 or l1
        # return dummy_head.next
        
        