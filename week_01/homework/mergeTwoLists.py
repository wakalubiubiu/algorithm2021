# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        protect = head
        while l1 or l2:
            if l2 is None or (l1 and l1.val <= l2.val):
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        return protect.next

    """
        head = ListNode(-1)
        protect = head
        while l1 or l2:
            if l2 is None or (l1 and l1.val <= l2.val):
                head.next = l1
                l1 = l1.next
                if l2 is None:
                    break
            else:
                head.next = l2
                l2 = l2.next
                if l1 is None:
                    break
            head = head.next
        return protect.next
    """


