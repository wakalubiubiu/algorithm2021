class Solution:
    # def myPow(self, x: float, n: int) -> float:
        # if n <0:
        #     x= 1/x
        #
        # def pow(x, n):
        #     if n==0:
        #         return 1
        #     elif n == -1:
        #         return x
        #     temp = pow(x, n//2)
        #     temp = temp * temp
        #     if n %2 == 1:
        #         temp *= x
        #     return temp
        # return pow(x, n)


    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n <0:
            return 1 / self.myPow(x, -n)
        temp = self.myPow(x, n//2)
        temp = temp * temp
        if n %2 == 1:
            temp *= x
        return temp


if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(2.0, 10))