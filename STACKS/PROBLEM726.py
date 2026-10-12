#NUMBER OF ATOMS 


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # STACK STORES ELEMENT COUNTS FOR EACH PARENTHESIZED GROUP
        stack = [{}]

        # CURRENT INDEX IN THE FORMULA
        i = 0

        # LENGTH OF THE FORMULA
        n = len(formula)

        # TRAVERSE THE FORMULA
        while i < n:
            # OPENING PARENTHESIS: START A NEW GROUP
            if formula[i] == "(":
                stack.append({})
                i += 1

            # CLOSING PARENTHESIS: FINISH THE CURRENT GROUP
            elif formula[i] == ")":
                # GET COUNTS INSIDE THE GROUP
                group = stack.pop()
                i += 1

                # READ THE MULTIPLIER AFTER ")"
                multiplier = 0
                while i < n and formula[i].isdigit():
                    multiplier = multiplier * 10 + int(formula[i])
                    i += 1

                # IF NO MULTIPLIER EXISTS, USE 1
                if multiplier == 0:
                    multiplier = 1

                # APPLY MULTIPLIER TO EVERY ELEMENT IN THE GROUP
                for atom, count in group.items():
                    stack[-1][atom] = stack[-1].get(atom, 0) + count * multiplier

            # READ AN ELEMENT SYMBOL
            else:
                # READ THE ELEMENT NAME
                start = i
                i += 1

                # ELEMENT NAMES START WITH AN UPPERCASE LETTER
                # AND MAY CONTINUE WITH LOWERCASE LETTERS
                while i < n and formula[i].islower():
                    i += 1

                atom = formula[start:i]

                # READ THE NUMBER AFTER THE ELEMENT
                count = 0
                while i < n and formula[i].isdigit():
                    count = count * 10 + int(formula[i])
                    i += 1

                # IF NO NUMBER EXISTS, COUNT IS 1
                if count == 0:
                    count = 1

                # ADD THE ELEMENT COUNT TO THE CURRENT GROUP
                stack[-1][atom] = stack[-1].get(atom, 0) + count

        # GET THE TOTAL COUNTS
        counts = stack[0]

        # BUILD THE FINAL ANSWER IN ALPHABETICAL ORDER
        answer = ""
        for atom in sorted(counts):
            answer += atom

            # APPEND THE COUNT ONLY IF IT IS GREATER THAN 1
            if counts[atom] > 1:
                answer += str(counts[atom])

        # RETURN THE FINAL CHEMICAL FORMULA
        return answer


# INPUT
formula = "Mg(OH)2"

# CREATE OBJECT
solution = Solution()

# CALL FUNCTION
result = solution.countOfAtoms(formula)

# OUTPUT
print("Number of Atoms:", result)
