#MAXIMUM NUMBER OF NON-OVERLAPPING SUBSTRINGS

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:

        # Step 1: Store the first and last occurrence
        # of every character
        first = {}
        last = {}

        for i, ch in enumerate(s):

            # Store the first occurrence
            if ch not in first:
                first[ch] = i

            # Update the last occurrence
            last[ch] = i

        # Step 2: Generate valid substring intervals
        intervals = []

        for ch in first:

            # Initial boundaries of the substring
            start = first[ch]
            end = last[ch]

            i = start
            valid = True

            # Expand the interval if necessary
            while i <= end:

                curr = s[i]

                # If a character starts before our interval,
                # this substring is invalid
                if first[curr] < start:
                    valid = False
                    break

                # Expand the ending boundary
                end = max(end, last[curr])

                i += 1

            # Store the valid interval
            if valid:
                intervals.append((start, end))

        # Step 3: Sort intervals by ending position
        intervals.sort(key=lambda x: x[1])

        # Step 4: Select non-overlapping intervals greedily
        result = []
        prev_end = -1

        for start, end in intervals:

            # Select the interval if it does not overlap
            if start > prev_end:

                result.append(s[start:end + 1])

                # Update the previous ending position
                prev_end = end

        # Step 5: Return the selected substrings
        return result


# -------------------------------
# Test cases
# -------------------------------

obj = Solution()

print(obj.maxNumOfSubstrings("adefaddaccc"))
# Output: ['e', 'f', 'ccc']

print(obj.maxNumOfSubstrings("abbaccd"))
# Output: ['bb', 'cc']