from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        count_dict = dict()
        count_dict[0] = 1
        ans = 0
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[i] + nums[i])
        for j in range(1, len(prefix_sum)):
            if prefix_sum[j]-k in count_dict:
                ans += count_dict[prefix_sum[j]-k]
            else:
                ans += 0
            if prefix_sum[j] in count_dict:
                count_dict[prefix_sum[j]] += 1
            else:
                count_dict[prefix_sum[j]] = 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.subarraySum([-1,-1,1], 0))