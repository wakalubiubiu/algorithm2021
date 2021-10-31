class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    206. 反转链表
    """
    def reverseList(self, head: ListNode) -> ListNode:
        # prev = None
        # while head:
        #     temp = head.next
        #     head.next = prev
        #     prev = head
        #     head = temp
        # return prev

        prev = None
        def recursion(prev, head):
            if not head:
                return prev
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            prev = recursion(prev, head)
            return prev
        prev = recursion(prev, head)

        return prev
