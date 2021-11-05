from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        queue = [start]
        change = ["A", "C", "G", "T"]
        visited = dict()
        # 最小层数放在哈希表中已经走过的节点上，这也是一个技巧，放在数组中也可以，我习惯用哈希表。这样在找它的下一层节点时，
        # 直接加1即可。
        visited[start] = 0
        while len(queue) > 0:
            node = queue[0]
            # 队列删除不要弄错，是删除队头，不是队尾。
            del queue[0]
            for i, char in enumerate(node):
                for j in change:
                    # 判断不要把一个位置改成它自己
                    if node[i] == j:
                        continue
                    string = node[0:i] + j + node[i+1:]
                    # 判断改完的参数是否在基因库中
                    if string not in bank:
                        continue
                    # 判断当前点是否已经访问过，需要访问最少层数，对同一个节点，肯定会是层数少的先到（也是判重）
                    if string in visited:
                        continue
                    depth = visited[node] + 1
                    # 如果找到直接返回
                    if string == end:
                        return depth
                    visited[string] = depth
                    queue.append(string)
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.minMutation("AAAACCCC", "CCCCCCCC", ["AAAACCCA","AAACCCCA","AACCCCCA", "AACCCCCC", "ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]))




