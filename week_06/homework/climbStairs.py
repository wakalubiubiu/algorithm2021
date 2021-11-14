class Solution:
    def climbStairs(self, n: int) -> int:
        climb = list()
        climb.append(0)
        climb.append(1)
        climb.append(2)
        for i in range(3, n+1):
            climb.append(climb[i-1] + climb[i-2])
        return climb[n]
