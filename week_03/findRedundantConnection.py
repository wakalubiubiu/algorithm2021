from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        visited_dict = dict()
        result = []
        now_path = [] 
        has_cycle = False

        def dfs(now_point, father):
            nonlocal now_path, has_cycle, result
            now_path.append(now_point)
            visited_dict[now_point] = True
            for point in to[now_point]:
                if has_cycle:
                    break
                if point == father:
                    continue
                if point not in visited_dict:
                    dfs(point, now_point)
                else:
                    location = now_path.index(point)
                    result = now_path[location:]
                    has_cycle = True
                    break
            now_path.remove(now_point)
            del visited_dict[now_point]

        for edge in edges:
            x = edge[0]
            y = edge[1]
            n = max(n, max(x, y))
        to = [[] for _ in range(n+1)]

        for edge in edges:
            to[edge[0]].append(edge[1])
            to[edge[1]].append(edge[0])
        dfs(1, 0)
        for edge in edges[::-1]:
            if edge[0] in result and edge[1] in result:
                return edge
        return []


if __name__ == '__main__':
    solution = Solution()
    print(solution.findRedundantConnection([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]))
