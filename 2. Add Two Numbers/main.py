from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstLN = ListNode(0)
        tail = firstLN
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1 and l1.val or 0
            val2 = l2 and l2.val or 0
            
            sum = val1 + val2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1 and l1.next or None
            l2 = l2 and l2.next or None

        result = firstLN.next

        return result