from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        amount_list = [0 for _ in range(amount+1)]
        amount_list[0] = 1
        for j in coins:
            for i in range(1, amount+1):
                if i-j >=0:
                    amount_list[i] += amount_list[i-j]
        return amount_list[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.change(5, [1, 2, 5]))