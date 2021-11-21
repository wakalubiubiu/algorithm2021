from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = len(nums)
        max_list = [0 for i in range(m)]
        max_list[0] = nums[0]
        max_sum = -(10 ** 4 + 1)
        for i in range(1, m):
            max_list[i] = max(max_list[i - 1] + nums[i], nums[i])

        for i in max_list:
            max_sum = max(max_sum, i)
        return max_sum