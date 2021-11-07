from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def validate(m, size):
            count = 1
            sum = 0
            for i in nums:
                if sum + i <= size:
                    sum += i
                else:
                    count +=1
                    sum = i
            # 最后这个return是我觉得非常非常不明白他在视频里说的一个东西，因为在视频课里讲的时候一直说的都是盒子的数量等于m是
            # 合法的，这里突然变成了盒子的数量小于m都是合法的，这让我感觉很突兀，后来自己想了一下，感觉稍微理解了一些，一个就是
            # 要把这个判断合法的函数用来做二分，这时如果想做高阶二分，就要保证是单调序，这样如果不是count<=m的话，这里就会出现
            # 一种情况，就是这个会变成 0,0,0,1,1,0,0这种情况，这样就没法用高阶二分了。例如示例中的【[1,4,4]，3】就是这种情况，
            # 这样在第一次判定中间值为6的时候就得出不符合的结论，之后的运行就都是错的了。
            return count <= m

        left = 0
        right = 0
        for i in nums:
            left = max(left, i)
            right +=i
        while left < right:
            mid = (left+right) // 2
            if validate(m, mid):
                right = mid
            else:
                left = mid + 1
        # 这是另一个重点之处，就是返回的是right这个值，这个是高阶二分查找返回指的写法，原因也就是只分为1组，左侧一直是不满足的
        # ，只有最右边一个数是满足的，所以返回最右侧最好。
        return right


if __name__ == '__main__':
    solution = Solution()
    print(solution.splitArray([1,4,4],  3))
