from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        max_spend_dict = dict()
        max_spend = 0
        min_spend_len = 99999
        for i in range(len(nums)):
            if nums[i] in max_spend_dict:
                max_spend_dict[nums[i]][1] = i
                max_spend_dict[nums[i]][2] += 1
            else:
                max_spend_dict[nums[i]] =[0, 0, 0]
                max_spend_dict[nums[i]][0] = i
                max_spend_dict[nums[i]][1] = i
                max_spend_dict[nums[i]][2] =1
        for key, value in max_spend_dict.items():
            if value[2] > max_spend:
                max_spend = value[2]
                min_spend_len = value[1]- value[0]+1
            elif value[2] == max_spend:
                min_spend_len = min(min_spend_len, value[1]- value[0]+1)
        return min_spend_len
