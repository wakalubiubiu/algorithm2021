from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = dict()
        count[5] = 0
        count[10] = 0
        count[20] = 0
        flag = True
        for bill in bills:
            count[bill] += 1
            need = bill -5
            if need > 0:
                for amount in [10,5]:
                    while need >= amount and count[amount] > 0:
                        need -= amount
                        count[amount] -= 1
                if need != 0:
                    flag = False
                    break
        return flag
