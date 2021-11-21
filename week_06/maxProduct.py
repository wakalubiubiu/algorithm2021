from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = len(nums)
        max_sum = -(10**9+1)
        max_list = [0 for i in nums]
        min_list = [0 for i in nums]
        max_list[0] = nums[0]
        min_list[0] = nums[0]
        for i in range(1, m):
            max_list[i] = max(max(max_list[i-1] * nums[i], min_list[i-1] * nums[i]), nums[i])
            min_list[i] = min(min(max_list[i-1] * nums[i], min_list[i-1] * nums[i]), nums[i])
        for i in max_list:
            max_sum = max(max_sum, i)
        return max_sum
