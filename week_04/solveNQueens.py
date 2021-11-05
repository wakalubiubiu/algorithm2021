from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = []
        ans_real = []
        now = []
        used = dict()
        used_plus = dict()
        used_minus = dict()

        def recursion(row):
            if row == n:
                ans.append(now[:])
                return
            for i in range(n):
                if i not in used and row-i not in used_plus and row + i not in used_minus:
                    now.append(i)
                    used[i] = 1
                    used_plus[row - i] = 1
                    used_minus[row + i] = 1
                    recursion(row+1)
                    now.pop()
                    del used[i]
                    del used_plus[row - i]
                    del used_minus[row + i]

        recursion(0)
        for i in ans:
            result = [['.' for _ in range(n)] for _ in range(n)]
            for m, j in enumerate(i):
                result[m][j] = 'Q'
            result = ["".join(local) for local in result]
            ans_real.append(result)

        return ans_real


if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(4))