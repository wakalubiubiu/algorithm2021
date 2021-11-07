from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        sum = [0]
        ans = 0
        # 前缀和是从0开始，到n的，所以这里的统计数组也应该是0~n，但是最后一个位置应该用不上,这又有另一个问题就是第二个for循环中
        # ，每次都要赋值，如果真用到了最后一个位置，count数组不写到n会报错，所以为了不特判，把这个count值写到n最好，但也不是所有
        # 示例都会用上，单调递增的就一定会用上。
        count = [0 for _ in range(len(nums)+1)]
        for i, e in enumerate(nums):
            sum.append(e % 2 + sum[i])
        for e in sum:
            # 因为要统计的是字段和中奇数个数等于k的个数，需要用的就是字段和s[j]-s[i]=k,得出 s[j] = s[i]，找出s[i]的个数即可。
            if e - k >= 0:
                ans += count[e - k]
            count[e] += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfSubarrays([1,1,2,1,1], 3))
