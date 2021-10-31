class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        protect_node = ListNode(0)
        protect_node.next = head
        last_node = protect_node
        while head:
            end = head
            count = k
            while end:
                count -= 1
                if count == 0:
                    break
                end = end.next
            if not end:
                break

            old_head = head
            next_group_head = end.next

            prev = None
            while head != next_group_head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp

            last_node.next = prev
            old_head.next = next_group_head
            last_node = old_head
            head = next_group_head

        return protect_node.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    solution = Solution()
    node = solution.reverseKGroup(node1, 2)
    print(node.val)




