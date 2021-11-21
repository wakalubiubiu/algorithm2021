from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        m = len(nums)
        result = [[0 for j in range(2)] for i in range(m+1)]
        ans = 0
        # 如果第一天不偷，那么就是result[1][1为0，这时由于赋初值ed时候全是0，所以不用修改，直接从2开始计算即可，表明第一天没有偷。
        for i in range(2, m+1):
            result[i][0] = max(result[i-1][1], result[i-1][0])
            result[i][1] = result[i-1][0] + nums[i-1]
        ans = max(result[m][0], result[m][1])
        # 第一天如果偷了，那么就是结果为result[1][1] = nums[0]，然后继续从2开始计算即可。
        result[1][1] = nums[0]
        for i in range(2, m+1):
            result[i][0] = max(result[i-1][1], result[i-1][0])
            result[i][1] = result[i-1][0] + nums[i-1]
        # 最后的时候要取第n天没有偷的结果，然后和第一天没有偷的结果进行比较，取其中的最大值即可。
        ans = max(ans, result[m][0])
        return ans