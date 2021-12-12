# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # head = ListNode()
        # protect = head
        # while l1 or l2:
        #     if l2 is None or (l1 and l1.val <= l2.val):
        #         head.next = l1
        #         l1 = l1.next
        #     else:
        #         head.next = l2
        #         l2 = l2.next
        #     head = head.next
        # return protect.next
        head = protect = ListNode(0)
        # while的过程思路很明确，就是谁小就把谁接到链表的结尾，直到有一个链表为空为止
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        # 这是存在一个情况，就是会有一个链表已经为空，通过这种方式把另一个链表接到结尾。此处的l1或者l2中有一个是空的，不会两个都是空或者都不空，因此可以不适用类似三目运算符的写法，而是直接用or即可。
        head.next = l1 or l2
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


