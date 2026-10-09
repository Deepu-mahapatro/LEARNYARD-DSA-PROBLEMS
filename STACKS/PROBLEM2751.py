#ROBOT COLLISIONS 


class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        # NUMBER OF ROBOTS
        n = len(positions)
        # STORE POSITION, HEALTH, DIRECTION, AND ORIGINAL INDEX
        robots = []
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])
        # SORT ROBOTS BY POSITION
        robots.sort()
        # STACK STORES INDICES OF SURVIVING ROBOTS IN SORTED ORDER
        stack = []
        # PROCESS EACH ROBOT FROM LEFT TO RIGHT
        for i in range(n):
            robot = robots[i]
            # COLLISION OCCURS WHEN PREVIOUS ROBOT MOVES RIGHT
            # AND CURRENT ROBOT MOVES LEFT
            while stack and robots[stack[-1]][2] == "R" and robot[2] == "L":
                # GET THE PREVIOUS ROBOT
                previous = robots[stack[-1]]
                # PREVIOUS ROBOT HAS GREATER HEALTH
                if previous[1] > robot[1]:
                    # PREVIOUS ROBOT LOSES ONE HEALTH
                    previous[1] -= 1
                    # CURRENT ROBOT IS DESTROYED
                    robot[1] = 0
                    break
                # BOTH ROBOTS HAVE EQUAL HEALTH
                elif previous[1] == robot[1]:
                    # BOTH ROBOTS ARE DESTROYED
                    stack.pop()
                    robot[1] = 0
                    break
                # CURRENT ROBOT HAS GREATER HEALTH
                else:
                    # PREVIOUS ROBOT IS DESTROYED
                    stack.pop()
                    # CURRENT ROBOT LOSES ONE HEALTH
                    robot[1] -= 1
                    # CHECK FOR ANOTHER COLLISION
            # ADD THE ROBOT IF IT SURVIVED
            if robot[1] > 0:
                stack.append(i)
        # COLLECT SURVIVING ROBOTS AS ORIGINAL INDEX AND HEALTH
        survivors = []
        for i in stack:
            survivors.append([robots[i][3], robots[i][1]])
        # RESTORE ORIGINAL INPUT ORDER
        survivors.sort()
        # RETURN ONLY THE SURVIVING HEALTHS
        answer = []
        for original_index, health in survivors:
            answer.append(health)
        return answer


# INPUT
positions = [3, 5, 2, 6]
healths = [10, 10, 15, 12]
directions = "RLRL"

# CREATE OBJECT
solution = Solution()

# CALL FUNCTION
result = solution.survivedRobotsHealths(positions, healths, directions)

# OUTPUT
print("Surviving Healths:", result)
