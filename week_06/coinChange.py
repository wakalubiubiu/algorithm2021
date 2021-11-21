from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.opt = list([10 ** 9]) * (amount + 1)
        self.opt[0] = 0

        def dfs(amount):
            if self.opt[amount] != 10 ** 9:
                return self.opt[amount]
            if amount < 0:
                return 10 ** 9
            if amount == 0:
                return 1
            else:
                for i in coins:
                    self.opt[amount] = min(dfs(amount - i) + 1, self.opt[amount])
                return self.opt[amount]

        count = dfs(amount)
        return count if count < 10 ** 9 else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange([2147483647], 2))