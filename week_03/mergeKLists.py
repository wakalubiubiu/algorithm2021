# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(-1)
        protect = head
        if len(lists) == 0:
            return protect.next
        if len(lists) == 1:
            return lists[0]
        l1 = self.mergeKLists(lists[0:len(lists)//2])
        l2 = self.mergeKLists(lists[len(lists)//2:])
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
