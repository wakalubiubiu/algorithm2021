from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        per_min = [0]
        sum_list = [0]
        max_sum = -1000000
        for i, e in enumerate(nums):
            sum_list.append(e + sum_list[i])
        for i in range(1, len(sum_list)):
            per_min.append(min(per_min[i-1], sum_list[i]))

        for i in range(1, len(sum_list)):
            # 此处注意是per_min[i-1]，是找出其前缀和中最小的值，以保证子序和最大。
            max_sum = max(max_sum, sum_list[i]- per_min[i-1])

        return max_sum


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-1]))