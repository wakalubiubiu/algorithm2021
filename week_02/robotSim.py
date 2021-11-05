from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = 0
        x = [0, 1, 0, -1]
        y = [1, 0, -1, 0]
        now_location = [0, 0]
        obstacles_dict = dict()
        max_distance = 0
        for obstacle in obstacles:
            obstacles_dict[str(obstacle[0]) + '_' + str(obstacle[1])] = 1
        for i in commands:
            if 1 <= i <= 9:
                for j in range(1, i+1):
                    location_x = now_location[0] + x[direction]
                    location_y = now_location[1] + y[direction]
                    if str(location_x) + '_' + str(location_y) in obstacles_dict:
                        break
                    now_location[0] = location_x
                    now_location[1] = location_y

            if i in [-1, -2]:
                rotation = -1 if i == -2 else 1
                direction = (direction + rotation) % 4
            max_distance = max(pow(now_location[0], 2) + pow(now_location[1], 2), max_distance)

        return max_distance


if __name__ == '__main__':
    solution = Solution()
    print(solution.robotSim([4, -1, 3], []))
