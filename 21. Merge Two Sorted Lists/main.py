# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        result = tail = ListNode()

        while list1 or list2:
            if (list1 is None or list1.val is None) and list2 is not None:
                tail.next = ListNode(list2.val)
                tail, list2 = tail.next, list2.next
                continue

            if (list2 is None or list2.val is None) and list1 is not None:
                tail.next = ListNode(list1.val)
                tail, list1 = tail.next, list1.next
                continue

            if list1.val < list2.val:
                tail.next = ListNode(list1.val)
                tail, list1 = tail.next, list1.next
            else:
                tail.next = ListNode(list2.val)
                tail, list2 = tail.next, list2.next

        return result.next
