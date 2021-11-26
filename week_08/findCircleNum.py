from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        self.fa = [0] * m

        for i in range(m):
            self.fa[i] = i
        for i, sub in enumerate(isConnected):
            for j, e in enumerate(sub):
                if e == 1:
                    self.union_set(i, j)

        count = 0
        for i, e in enumerate(self.fa):
            if self.fa[i] == i:
                count += 1
        return count

    def find(self, x):
        if x == self.fa[x]:
            return x
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union_set(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.fa[x] = y


if __name__ == '__main__':
    solution = Solution()
    solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])