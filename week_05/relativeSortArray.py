from functools import cmp_to_key
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_list = [0 for _ in range(1001)]
        result = []
        for i, e in enumerate(arr1):
            count_list[e] += 1
        for i, e in enumerate(arr2):
            while count_list[e] >0:
                result.append(e)
                count_list[e] -= 1
        for i, e in enumerate(count_list):
            while e >0:
                result.append(i)
                e -= 1
        return result
        # arr_map = dict()
        # for i, arr in enumerate(arr2):
        #     arr_map[arr] = i
        #
        # def cus_sorted(x, y):
        #     pos_x = arr_map[x] if x in arr_map else len(arr2)
        #     pos_y = arr_map[y] if y in arr_map else len(arr2)
        #
        #     flag = (pos_x < pos_y) or (pos_x == pos_y and x<y)
        #     print("-----", x, y, flag)
        #     # 此处反过来了，很奇怪
        #     return 1 if not flag else -1
        #
        # new_arr = sorted(arr1, key=cmp_to_key(cus_sorted))
        # return new_arr


if __name__ == '__main__':
    solution = Solution()
    print(solution.relativeSortArray([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]))

    # [22, 28, 8, 6, 17, 44]
