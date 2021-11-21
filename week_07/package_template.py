from typing import List


class Solution:
    def package_template(self, things: List[int], values: List[int], limit: int) -> int:
        ans = 0
        m = len(things)
        package_list = [0 for _ in range(limit+1)]
        for i in range(1, m+1):
            # 每次循环的时候都会将上一次中体积相同，但是价值低的替换掉
            # 此处使用的是倒序循环，和三角形最小路径和那个思路一致，因为从前往后更新会让本来需要使用的值被覆盖掉，而从后
            # 往前更新则会保留原值。
            for j in range(limit, things[i-1]-1, -1):
                package_list[j] = max(package_list[j], package_list[j-things[i-1]] + values[i-1])

        for i in package_list:
            ans = max(ans, i)
        # print(package_list[len(things)-1][0:limit+1])
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.package_template([3, 1, 4, 5, 7], [2, 9, 7, 4, 1], 10))
