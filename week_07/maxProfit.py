from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.insert(0, 0)
        n = len(prices)
        f = [[-10**5, -10**5] for _ in prices]
        f[0][0] = 0
        for i in range(1, len(prices)):
            f[i][1] = max(f[i][1], f[i-1][0] - prices[i])
            f[i][0] = max(f[i][0], f[i-1][1] + prices[i])
            for j in range(2):
                f[i][j] = max(f[i][j], f[i-1][j])
        return f[n-1][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
