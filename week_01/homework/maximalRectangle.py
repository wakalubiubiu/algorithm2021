from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        max_area = 0
        matrix.append(['0' for _ in range(n)])
        left = [[0 for _ in row] for row in matrix]

        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value == '1':
                    left[i][j] = (0 if j == 0 else left[i][j-1]) + 1
        for j in range(n):
            stack = []
            for i in range(m+1):
                relative_width = 0
                while len(stack) > 0 and left[i][j] <= stack[-1][1]:
                    relative_width += stack[-1][0]
                    max_area = max(max_area, relative_width * stack[-1][1])
                    stack.pop()
                stack.append((relative_width + 1, left[i][j]))

        return max_area


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximalRectangle([["1"]]))
