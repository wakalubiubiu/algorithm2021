from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        to = [[] for _ in range(numCourses)]
        degrees = [0 for _ in range(numCourses)]
        queue = []
        lesson = []
        for edge in prerequisites:
            to[edge[1]].append(edge[0])
            degrees[edge[0]] += 1
        for i, deg in enumerate(degrees):
            if deg == 0:
                queue.append(i)
        while len(queue) > 0:
            point = queue[0]
            del queue[0]
            lesson.append(point)
            for next_point in to[point]:
                degrees[next_point] -= 1
                if degrees[next_point] == 0:
                    queue.append(next_point)

        return len(lesson) == numCourses


if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(2, [[1, 0]]))
