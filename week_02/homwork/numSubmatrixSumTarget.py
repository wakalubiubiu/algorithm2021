from collections import Counter
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # sum = [[0]*(len(matrix[0])+1)]*(len(matrix)+1)
        sum = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        count = 0
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0]) + 1):
                sum[i][j] = sum[i][j-1]+ sum[i-1][j] -sum[i-1][j-1] + matrix[i-1][j-1]
                for m in range(1, i+1):
                    for n in range(1, j+1):
                        sub_sum = sum[i][j] - sum[m-1][j] - sum[i][n-1] + sum[m-1][n-1]
                        if sub_sum == target:
                            count +=1
        return count


    def numSubmatrixSumTarget_2(self, matrix: List[List[int]], target: int) -> int:
        def subarraySum(nums: List[int], k: int) -> int:
            mp = Counter([0])
            count = pre = 0
            for x in nums:
                pre += x
                if pre - k in mp:
                    count += mp[pre - k]
                mp[pre] += 1
            return count

        m, n = len(matrix), len(matrix[0])
        ans = 0
        # 枚举上边界
        for i in range(m):
            total = [0] * n
            # 枚举下边界
            for j in range(i, m):
                for c in range(n):
                    # 更新每列的元素和
                    total[c] += matrix[j][c]
                ans += subarraySum(total, target)

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSubmatrixSumTarget([[904]], 0))