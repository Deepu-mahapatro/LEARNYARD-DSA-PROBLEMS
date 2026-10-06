#ASTEROID COLLISION

# ASTEROID COLLISION

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        # STACK STORES SURVIVING ASTEROIDS
        stack = []

        # TRAVEL THROUGH EACH ASTEROID
        for asteroid in asteroids:
            # CHECK IF COLLISION IS POSSIBLE
            # TOP ASTEROID MOVES RIGHT
            # CURRENT ASTEROID MOVES LEFT
            while stack and stack[-1] > 0 and asteroid < 0:
                # CURRENT ASTEROID IS BIGGER
                if abs(asteroid) > stack[-1]:
                    # REMOVE TOP ASTEROID
                    stack.pop()

                # BOTH ASTEROIDS HAVE SAME SIZE
                elif abs(asteroid) == stack[-1]:
                    # REMOVE TOP ASTEROID
                    stack.pop()
                    # CURRENT ASTEROID ALSO EXPLODES
                    break

                # TOP ASTEROID IS BIGGER
                else:
                    # CURRENT ASTEROID EXPLODES
                    break

            else:
                # CURRENT ASTEROID SURVIVED
                # ADD IT TO THE STACK
                stack.append(asteroid)

        # RETURN SURVIVING ASTEROIDS
        return stack
# INPUT
asteroids = [5, 10, -5]

# CREATE OBJECT
solution = Solution()

# CALL FUNCTION
result = solution.asteroidCollision(asteroids)

# OUTPUT
print("Surviving Asteroids:", result)