class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        protect_node = ListNode(0)
        protect_node.next = head
        # 上一组翻转的k个节点的最后一个节点
        last_node = protect_node
        while head:
            end = head
            count = k
            while end:
                # 此处count值先减1，然后判断是否不等于0，再更新end成为下一个节点。这样的话由于先count，最后的end就是当前需要翻转的最后一个节点。
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

            # 上一组最后一个节点等于这一组翻转完的最后一个节点，就是prev
            last_node.next = prev
            # 本组翻转的第一个节点已经变成了k个节点的最后一个节点，因此需要指向下一组的开头
            old_head.next = next_group_head
            # 进行下一组翻转前，需要把last_node更新为本组最后一个节点，也就是翻转本组k个节点的第一个节点。
            last_node = old_head
            # 把head节点更新为下一组的开头，然后继续进行下一组的翻转
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
    node = solution.reverseKGroup(node1, 3)
    print(node.val)
