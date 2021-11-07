# Definition for singly-linked list.
from heapq import heappush, heappop
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class CustomHeapq:
    def __init__(self):
        self.list = [ListNode(-10**4-1)]

    def get_min(self):
        if len(self.list) > 1:
            return self.list[1]
        else:
            return None

    def is_empty(self):
        return len(self.list) == 1

    def insert(self, listNode: ListNode):
        self.list.append(listNode)
        self.heapifyup(len(self.list)-1)

    def delete(self):
        self.list[1] = self.list[len(self.list) - 1]
        self.list.pop()
        self.heapifydown(1)

    def heapifyup(self, p):
        while p > 1:
            if self.list[p].val < self.list[p//2].val:
                self.list[p], self.list[p//2] = self.list[p//2], self.list[p]
                p = p//2
            else:
                break

    def heapifydown(self, p):
        child = p*2
        while child < len(self.list):
            other = p*2 +1
            # 这是一个小技巧，就是如果需要交换，每次都是让p和child交换，不必再去判断，是和child还是和other交换，先让他们判断，
            # 然后把小的放到child。
            if other < len(self.list) and self.list[other].val < self.list[child].val:
                child = other
            if self.list[child].val < self.list[p].val:
                self.list[child], self.list[p] = self.list[p], self.list[child]
                # p要变成它自己的child元素，因此这里需要赋值
                p = child
                # p变成child之后它的child就是当前位置再乘以2，因此是p*2.注意这里不要忘记，忘记了会出现很奇怪的错误，不好调试。
                child = p*2
            else:
                break


class Solution:
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     h = []
    #     for list_node in lists:
    #         if list_node:
    #             heappush(h, (list_node.val, list_node))
    #     head = ListNode(-10**4-1)
    #     tail = head
    #     while len(h) > 0:
    #         node_tuple = heappop(h)
    #         tail.next = node_tuple[1]
    #         tail = tail.next
    #         node_new = node_tuple[1].next
    #         if node_new:
    #             heappush(h, (node_new.val, node_new))
    #
    #     return head.next
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        custom_heapq = CustomHeapq()
        for list_node in lists:
            if list_node:
                custom_heapq.insert(list_node)
        head = ListNode(-10**4-1)
        tail = head
        while not custom_heapq.is_empty():
            node = custom_heapq.get_min()
            custom_heapq.delete()
            tail.next = node
            tail = tail.next
            node_new = node.next
            if node_new:
                custom_heapq.insert(node_new)

        return head.next


if __name__ == '__main__':
    list_node_1 = ListNode(1)
    list_node_4 = ListNode(4)
    list_node_5 = ListNode(5)
    list_node_1.next = list_node_4
    list_node_4.next = list_node_5
    list_node_21 = ListNode(1)
    list_node_24 = ListNode(3)
    list_node_25 = ListNode(4)
    list_node_21.next = list_node_24
    list_node_24.next = list_node_25
    list_node_32 = ListNode(2)
    list_node_36 = ListNode(6)
    list_node_32.next = list_node_36

    solution =Solution()
    list_node = solution.mergeKLists([list_node_1, list_node_21, list_node_32])
    while list_node:
        print(str(list_node.val) + '->', end='')
        list_node = list_node.next
