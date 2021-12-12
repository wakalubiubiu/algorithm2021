from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        m = len(nums)
        sum_list = [0]
        dequeue = []
        ans = -(10 ** 9)
        # 循环两次，求前缀和。
        for i, e in enumerate(nums):
            sum_list.append(sum_list[i] + nums[i])
        for i, e in enumerate(nums):
            sum_list.append(sum_list[m + i] + nums[i])
        for i, e in enumerate(sum_list):
            # 利用单调队列的思想，保持一个滑动窗口，如果滑动窗口最左侧的下标已经超出了滑动窗口的左边界，需要删除。此处的滑动
            # 窗口最多需要保持n的元素，而这时如果滑动窗口的大小真的为n，那么队列的第一个元素就是和i一样的元素，这样在计算子序和
            # 的时候相减正好计算的字段和就是从队列中第一个元素i的下标之后的元素开始的字段和，因此滑动窗口的大小为n。这个地方有点困惑，需要多理解
            while len(dequeue) > 0 and dequeue[0] < i - m:
                del dequeue[0]
            if len(dequeue) > 0:
                ans = max(ans, e - sum_list[dequeue[0]])
            while len(dequeue) > 0 and sum_list[dequeue[-1]] > e:
                del dequeue[-1]
            dequeue.append(i)
        return ans


if __name__ == '__main__':
    solution = Solution()
    solution.maxSubarraySumCircular([1, 2, 3, 4])