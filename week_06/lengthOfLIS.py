from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m = len(nums)
        max_lis = 1
        max_lis_list = [1 for i in nums]
        for i in range(1, m):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    max_lis_list[i] = max(max_lis_list[i], max_lis_list[j] + 1)
        for i in max_lis_list:
            max_lis = max(max_lis, i)
        return max_lis
