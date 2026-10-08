#SIMPLIFY PATH 

# SIMPLIFY PATH

class Solution:
    def simplifyPath(self, path: str) -> str:
        # STACK STORES VALID DIRECTORY NAMES
        stack = []
        # SPLIT PATH INTO INDIVIDUAL PARTS
        parts = path.split("/")
        # TRAVERSE THROUGH EACH PART
        for part in parts:
            # IGNORE EMPTY PARTS AND CURRENT DIRECTORY "."
            if part == "" or part == ".":
                continue
            # ".." MEANS GO TO THE PARENT DIRECTORY
            elif part == "..":
                # POP ONLY IF A DIRECTORY EXISTS
                if stack:
                    stack.pop()
            # NORMAL DIRECTORY NAME
            else:
                # ADD DIRECTORY TO STACK
                stack.append(part)
        # JOIN DIRECTORIES AND ADD "/" AT THE BEGINNING
        return "/" + "/".join(stack)


# INPUT
path = "/home/user/../documents/"

# CREATE OBJECT
solution = Solution()

# CALL FUNCTION
result = solution.simplifyPath(path)

# OUTPUT
print("Simplified Path:", result)