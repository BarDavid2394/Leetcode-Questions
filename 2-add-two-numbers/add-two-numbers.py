# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = current = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1=l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry,10)
            current.next = ListNode(val)
            current = current.next
        return dummy.next




















        # if l1 is None:
        #     return l2
        # if l2 is None:
        #     return l1
        # dummy_head = ListNode()
        # current, carry, value1, value2 = dummy_head, 0,0,0
        # while l1 or l2 or carry:
        #     if(l1):
        #         value1 = l1.val
        #     else:
        #         value1 = 0
        #     if(l2):
        #         value2 = l2.val
        #     else:
        #         value2 = 0
        #     #  if l1 else 0
        #     # l2.val = l2.val if l2 else 0
        #     total_sum = value1 + value2 + carry
        #     carry = total_sum // 10
        #     current.next = ListNode(total_sum % 10)
        #     current = current.next
        #     if l1:
        #         l1 = l1.next
        #     if l2:
        #         l2 = l2.next
        # return dummy_head.next
        

        