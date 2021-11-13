from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        shagnse = True
        visited = [[0 for _ in range(len(sub_list))] for sub_list in board]

        now_visited = [[0 for _ in range(len(sub_list))] for sub_list in board]

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        def dfs(i, j):
            nonlocal shagnse
            queue = []
            queue.append([i, j])
            now_visited[i][j] = 1
            while len(queue) > 0:
                node = queue[0]
                del queue[0]
                for direction in range(4):
                    new_x = i + dx[direction]
                    new_y = j + dy[direction]
                    if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n or board[new_x][new_y] == 'X':
                        continue
                    if new_x == m or new_y == n:
                        shangse = False
                    if visited[new_x][new_y] != 0 or now_visited[new_x][new_y] != 0:
                        continue
                    queue.append([new_x, new_y])
                    now_visited[new_x][new_y] = 1

        for i, sub_list in enumerate(board):
            for j, e in enumerate(sub_list):
                if visited[i][j] == 0 and e != 'X':
                    dfs(i, j)
                    value = 1 if shagnse else 2
                    for i, sub_list in enumerate(now_visited):
                        for j, e in enumerate(sub_list):
                            if e == 1:
                                visited[i][j] = value
                            now_visited[i][j] = 0

        for i, sub_list in enumerate(board):
            for j, e in enumerate(sub_list):
                if visited[i][j] == 1:
                    board[i][j] = 'X'