from functools import cmp_to_key
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def custom_sort(x, y):
            # 这个自定义排序的函数返回很有说法，需要研究一下，返回true或者false不行，需要返回1或者-1。
            flag = x[0]<y[0] or (x[0]==y[0] and x[1]<y[1])
            return 1 if not flag else -1
        ans = []
        sorted_list = sorted(intervals, key=cmp_to_key(custom_sort))
        # start记录当前还未完成合并的区间左端点的位置
        start = -1
        # end记录当前还未完成合并的区间右端点的位置
        end = -1
        for sub_list in sorted_list:
            left = sub_list[0]
            right = sub_list[1]
            # 排好序后，也不会出现后一个区间全包围前一个区间的情况，因此在比较时，只需要比较后一个区间的左端点是否在现在记录的
            # 未合并的右端点之前即可，如果在，那么就是有重叠。
            if left <= end:
                # 如果存在重叠，需要比较一下当前的区间的右端点和已经记录的未合并完成的右端点谁更靠右，更新为更靠右的端点。
                end = right if end<=right else end
            else:
                # 如果不存在重叠，并且上一次区间不是初始用来判断的区间，那么就需要将其加入答案，并且把当前区间更新为待合并区间，
                # 用于对下一个区间的判断
                if end != -1:
                    ans.append([start, end])
                start = left
                end = right
        # 最后一组需要放在外面写进ans，因为for循环已经知完毕了
        ans.append([start, end])
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([[1, 3], [8, 10], [2, 6], [15, 18]]))

