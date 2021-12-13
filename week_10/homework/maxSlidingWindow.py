from typing import List
from sortedcontainers import SortedDict


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        d = SortedDict()
        for i in nums[0:k]:
            d[i] = d.get(i, 0) + 1
        result.append(d.peekitem(-1)[0])
        for i in range(k, len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1
            d[nums[i-k]] -= 1
            if d[nums[i-k]] == 0:
                del d[nums[i-k]]
            result.append(d.peekitem(-1)[0])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
