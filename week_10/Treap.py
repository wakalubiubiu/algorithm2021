import random


class Node:
    def __init__(self, data):
        self.key = data
        self.val = random.randint(1, int(1e9))
        self.cnt = self.size = 1
        self.left = self.right = None


class Treap:

    def __init__(self):
        self.root = Node(int(-1e9))
        self.root.right = Node(int(1e9))
        self._update(self.root)

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def remove(self, data):
        self.root = self._remove(self.root, data)

    def get_rank_by_val(self, target):
        return self._get_rank_by_val(self.root, target) - 1

    def get_val_by_rank(self, rank):
        return self._get_val_by_rank(self.root, rank + 1)

    def get_pre(self, target):
        ans = int(-1e9)
        p = self.root
        while p:
            if target == p.key:
                if p.left:
                    p = p.left
                    while p.right:
                        p = p.right
                break
            if target > p.key > ans:
                ans = p.key
            p = p.left if target < p.key else p.right

        return ans

    def get_next(self, target):
        ans = int(1e9)
        p = self.root
        while p:
            if target == p.key:
                if p.right:
                    p = p.right
                    while p.left:
                        p = p.left
                    ans = p.key
                break
            if target < p.key < ans:
                ans = p.key
            p = p.left if target < p.key else p.right
        return ans

    def _get_rank_by_val(self, p, target):
        if not p:
            return 0
        left_size = p.left.size if p.left else 0
        if target == p.key:
            return left_size + 1
        if target < p.key:
            return self._get_rank_by_val(p.left, target)
        return left_size + p.cnt + self._get_rank_by_val(p.right, target)

    def _get_val_by_rank(self, p, rank):
        if not p:
            return int(1e9)
        left_size = p.left.size if p.left else 0
        if left_size >= rank:
            return self._get_val_by_rank(p.left, rank)
        if left_size + p.cnt >= rank:
            return p.key
        return self._get_val_by_rank(p.right, rank - left_size - p.cnt)

    def _insert(self, p, data):
        res = p
        if not p:
            res = Node(data)
        elif data == p.key:
            p.cnt += 1
        elif data < p.key:
            p.left = self._insert(p.left, data)
            if p.val < p.left.val:
                res = self._zig(p)
        else:
            p.right = self._insert(p.right, data)
            if p.val < p.right.val:
                res = self._zag(p)
        self._update(res)
        return res

    def _remove(self, p, data):
        if not p:
            return None
        if data == p.key:
            if p.cnt > 1:
                p.cnt -= 1
                self._update(p)
                return p
            if not p.left and not p.right:
                return None
            res = p
            if not p.right or (p.left and p.left.key > p.right.key):
                res = self._zig(p)
                res.right = self._remove(res.right, data)
            else:
                res = self._zag(p)
                res.left = self._remove(res.left, data)
            if res:
                self._update(res)
            return res
        if data < p.key:
            p.left = self._remove(p.left, data)
        else:
            p.right = self._remove(p.right, data)
        if p:
            self._update(p)
        return p

    def _zig(self, p):
        q = p.left
        p.left = q.right
        q.right = p
        self._update(p)
        self._update(q)
        return q

    def _zag(self, p):
        q = p.right
        p.right = q.left
        q.left = p
        self._update(p)
        self._update(q)
        return q

    def _update(self, p):
        left_size = p.left.size if p.left else 0
        right_size = p.right.size if p.right else 0
        p.size = left_size + right_size + p.cnt


if __name__ == '__main__':
    n = int(input())
    treap = Treap()
    while n:
        opt, x = map(int, input().split())
        if opt == 1:
            treap.insert(x)
        elif opt == 2:
            treap.remove(x)
        elif opt == 3:
            print(treap.get_rank_by_val(x))
        elif opt == 4:
            print(treap.get_val_by_rank(x))
        elif opt == 5:
            print(treap.get_pre(x))
        elif opt == 6:
            print(treap.get_next(x))
        n -= 1

