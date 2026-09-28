class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_depth = 0

        for i in range(len(s)):
            if s[i] == "(":
                count += 1
                max_depth = max(max_depth, count)

            elif s[i] == ")":
                count -= 1

        return max_depth