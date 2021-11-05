from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        now_array = []
        used = dict()

        def recursion():
            if len(now_array) == len(nums):
                ans.append(now_array[:])
                return
            for i in range(0, len(nums)):
                if nums[i] in used:
                    continue
                used[nums[i]] = 1
                now_array.append(nums[i])
                recursion()
                now_array.pop()
                del used[nums[i]]
        recursion()
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
