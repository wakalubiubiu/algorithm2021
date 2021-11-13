from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        new_g = sorted(g)
        new_s = sorted(s)
        j = 0
        ans = 0
        for e in new_g:
            # 此处while循环的意义就是找到第一块满足的饼干发给孩子。此处有个细节，while循环最后一次的时候，要么代表一块都没有，
            # 要么代表找到了一块，如果是找到了一块，下一个if判断的时候也要加j +=1，表明发出了这块饼干，这个地方开始想错了。
            while j < len(s) and new_s[j] < e:
                j += 1
            # 如果进入了if循环，就说明存在饼干满足小孩。
            if j < len(s):
                j += 1
                ans += 1
        return ans
