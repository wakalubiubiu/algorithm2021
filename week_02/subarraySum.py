from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_sum = dict()
        total = ans = 0
        hash_sum[0] = 1
        for i in nums:
            total += i
            if total - k in hash_sum:
                ans += hash_sum[total - k]
            if total in hash_sum:
                hash_sum[total] += 1
            else:
                hash_sum[total] = 1
        return ans

        # d = {}
        # acc = count = 0
        # for num in nums:
        #     acc += num
        #     if acc == k:
        #         count += 1
        #     if acc - k in d:
        #         count += d[acc - k]
        #     if acc in d:
        #         d[acc] += 1
        #     else:
        #         d[acc] = 1
        # return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.subarraySum([-1, -1, 1], 0))
