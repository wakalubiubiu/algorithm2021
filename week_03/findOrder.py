from typing import List


class Solution:
    """
    210. 课程表 II
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        to_list = [[] for _ in range(numCourses)]
        queue = []
        deg_list = [0 for _ in range(numCourses)]
        course_list = []
        for sub_list in prerequisites:
            to_list[sub_list[1]].append(sub_list[0])
            deg_list[sub_list[0]] +=1
        for i, deg in enumerate(deg_list):
            if deg == 0:
                queue.append(i)
        while len(queue) != 0:
            pre_course = queue.pop(0)
            course_list.append(pre_course)
            for follow_course in to_list[pre_course]:
                deg_list[follow_course] -= 1
                if deg_list[follow_course] == 0:
                    queue.append(follow_course)
        if len(course_list) == numCourses:
            return course_list
        else:
            return []


if __name__ == '__main__':
    solution = Solution()
    print(solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))