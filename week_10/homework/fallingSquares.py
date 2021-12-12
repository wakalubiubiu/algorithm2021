from typing import List


class Node:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.height = 0
        self.mark = 0


class SegmentTree:
    def __init__(self, m):
        self.segment_list = [Node() for _ in range(4 * m + 1)]
        self.build(1, 0, m - 1)

    def build(self, location, left, right):
        self.segment_list[location].left = left
        self.segment_list[location].right = right
        if left == right:
            self.segment_list[location].height = 0
            return
        mid = (left + right) // 2
        self.build(2 * location, left, mid)
        self.build(2 * location + 1, mid + 1, right)
        self.segment_list[location].height = max(self.segment_list[2 * location].height, self.segment_list[2 * location + 1].height)

    def query(self, location, left, right):
        if left <= self.segment_list[location].left and self.segment_list[location].right <= right:
            return self.segment_list[location].height
        ans = 0
        self.spread(location)
        mid = (self.segment_list[location].left + self.segment_list[location].right) // 2
        if left <= mid:
            ans = max(ans, self.query(location * 2, left, right))
        if right > mid:
            ans = max(ans, self.query(location * 2 + 1, left, right))
        return ans

    def changeRange(self, curr, left, right, delta):
        # 完全包含
        if left <= self.segment_list[curr].left and right >= self.segment_list[curr].right:
            # 修改这个被完全包含的区间的信息
            self.segment_list[curr].height = delta
            # 子树不改了，有bug，标记一下
            self.segment_list[curr].mark = delta
            return
        self.spread(curr)
        mid = (self.segment_list[curr].left + self.segment_list[curr].right) >> 1
        if left <= mid:
            self.changeRange(curr * 2, left, right, delta)
        if right > mid:
            self.changeRange(curr * 2 + 1, left, right, delta)
        self.segment_list[curr].height = max(self.segment_list[curr * 2].height,
                                             self.segment_list[curr * 2 + 1].height)

    def spread(self, curr):
        if self.segment_list[curr].mark != 0:
            self.segment_list[curr * 2].height = self.segment_list[curr].mark
            self.segment_list[curr * 2].mark = self.segment_list[curr].mark
            self.segment_list[curr * 2 + 1].height = self.segment_list[curr].mark
            self.segment_list[curr * 2 + 1].mark = self.segment_list[curr].mark
            self.segment_list[curr].mark = 0


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        """
        一杯茶水一包烟，一道习题做一天
        """
        self.list = []
        ans = []
        max_height = 0
        for position in positions:
            self.list.append(position[0])
            self.list.append(position[0] + position[1])
        self.list = sorted(self.list)
        self.m = 0
        for i, e in enumerate(self.list):
            if i == 0 or e != self.list[i - 1]:
                self.list[self.m] = e
                self.m += 1
        segmentTree = SegmentTree(self.m)
        for position in positions:
            left = self.get_hash_value(position[0]) + 1
            right = self.get_hash_value(position[1] + position[0])
            value = segmentTree.query(1, left, right)
            max_height = max(max_height, value + position[1])
            ans.append(max_height)
            segmentTree.changeRange(1, left, right, value + position[1])
        return ans

    def get_hash_value(self, value):
        left = 0
        right = self.m - 1
        while left <= right:
            mid = (left + right) // 2
            if value == self.list[mid]:
                return mid
            if value < self.list[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
