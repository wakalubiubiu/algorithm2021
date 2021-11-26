from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        dx = [0, 1]
        dy = [1, 0]
        fa = [i for i in range(0, m * n + 1)]

        def find(x):
            if x == fa[x]:
                return x
            fa[x] = find(fa[x])
            return fa[x]

        def union_set(x, y):
            x = find(x)
            y = find(y)
            if x != y:
                fa[x] = y

        for i, sub in enumerate(board):
            for j, e in enumerate(sub):
                if e == 'X':
                    continue
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    union_set(i * n + j, m * n)
                for direction in range(2):
                    new_x = i + dx[direction]
                    new_y = j + dy[direction]
                    if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == 'O':
                        union_set(i * n + j, new_x * n + new_y)
        outside = find(m * n)
        for i, sub in enumerate(board):
            for j, e in enumerate(sub):
                if e == 'O' and find(i * n + j) != outside:
                    board[i][j] = 'X'


