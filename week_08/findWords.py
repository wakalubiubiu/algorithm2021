from typing import List


class Node:
    def __init__(self):
        self.count = 0
        self.children = {}


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        self.root = Node()
        ans = set()
        self.chosen = ''
        visited = [[0]*n for _ in range(m)]

        def dfs(x, y, current):
            ch = board[x][y]
            if ch not in current.children:
                return
            self.chosen += ch
            child = current.children[ch]
            # print(self.chosen)
            # if self.chosen == 'eat':
                # print(child)
            if child.count > 0:
                ans.add(self.chosen)
            for direction in range(4):
                new_x = x + dx[direction]
                new_y = y + dy[direction]
                if 0 <= new_x < m and 0 <= new_y < n:
                    if visited[new_x][new_y] == 0:
                        visited[new_x][new_y] = 1
                        dfs(new_x, new_y, child)
                        visited[new_x][new_y] = 0
            self.chosen = self.chosen[0:-1]

        for word in words:
            self.insert(word)
        for i, sub in enumerate(board):
            for j, e in enumerate(sub):
                visited[i][j] = 1
                dfs(i, j, self.root)
                visited[i][j] = 0
        return list(ans)

    def insert(self, word):
        current = self.root
        for word_ch in word:
            if word_ch not in current.children:
                current.children[word_ch] = Node()
            current = current.children[word_ch]
        current.count += 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.findWords(
        [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
        ["oath", "pea", "eat", "rain"]))
