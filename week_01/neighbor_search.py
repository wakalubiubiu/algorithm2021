"""
临值查找
"""
from collections import OrderedDict


class ListNode:
    def __init__(self, x, y):
        self.val = x
        self.location = y
        self.next = None
        self.prev = None

    def add_Node(self, prev):
        prev.next.prev = self
        self.next = prev.next
        self.prev = prev
        prev.next = self

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev


if __name__ == '__main__':
    rank = [0]
    nums = [0]
    n = input("")
    n = int(n)
    number_str = input("")
    d = OrderedDict()
    for number in number_str.split(" "):
        try:
            nums.append(int(number))
        except:
            continue
    for i in range(1, n + 1):
        rank.append(i)

    pos = [ListNode(0, 0) for _ in range(0, n + 1)]
    ans = [0 for _ in range(0, n + 1)]
    rank = sorted(rank[1:], key=lambda x: nums[x])
    rank.insert(0, nums[rank[n - 1]] + 10 ** 9)
    sorted_list = sorted(nums)
    head = ListNode(nums[rank[1]] - 10 ** 9, None)
    tail = ListNode(nums[rank[n]] + 10 ** 9, None)

    head.next = tail
    tail.prev = head

    for i in range(1, n + 1):
        node = ListNode(nums[rank[i]], rank[i])
        node.add_Node(tail.prev)
        pos[rank[i]] = node

    for i in range(n, 1, -1):
        node = pos[i]
        ans[i] = (
            node.prev.location if (node.val - node.prev.val) <= (node.next.val - node.val) else node.next.location)
        node.delete()

    for i in range(2, n + 1):
        print(abs(nums[ans[i]] - nums[i]), ans[i])
