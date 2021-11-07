from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 因为前缀和计算的是1到len(bookings)， 所以差分的数字的长度要比len(bookings)大1，因为python的range的特点，所以此处要+2。
        delta_list = [0 for _ in range(n+2)]
        # 和就是要求1~n个航班的数字，所以此处就从0开始到n，写为n+1
        sum_list = [0 for _ in range(n+1)]
        for sub_list in bookings:
            # 差分改的两个位置，第一个改变的数字的位置，和最后一个改变的数字的后一个位置。
            delta_list[sub_list[0]] += sub_list[2]
            delta_list[sub_list[1]+1] -= sub_list[2]
        # 计算前缀和，只需要计算前n个即可，
        for i in range(1, n+1):
            sum_list[i] = sum_list[i-1] + delta_list[i]

        # 答案需要从1开始
        return sum_list[1:]


if __name__ == '__main__':
    solution = Solution()
    print(solution.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))
