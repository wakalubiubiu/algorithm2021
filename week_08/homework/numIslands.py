from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [0, 1]
        dy = [1, 0]
        ans = 0
        row_size = len(grid)
        cols_size = len(grid[0])
        self.fa = [i for i in range(row_size * cols_size)]
        for i, sub_list in enumerate(grid):
            for j, element in enumerate(sub_list):
                if element == '1':
                    for direction in range(2):
                        new_x = i + dx[direction]
                        new_y = j + dy[direction]
                        if new_x < row_size and new_y < cols_size and grid[new_x][new_y] == '1':
                            self.union_set(i * cols_size + j, new_x * cols_size + new_y)
        for i, sub_list in enumerate(grid):
            for j, element in enumerate(sub_list):
                if i * cols_size + j == self.fa[i * cols_size + j] and element == '1':
                    ans += 1
        return ans

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