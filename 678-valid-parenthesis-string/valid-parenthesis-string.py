class Solution:
    def checkValidString(self, s: str) -> bool:
        #O(n),O(1)
        low = 0
        high = 0
        for ch in s:
            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1       # '*' as ')'
                high += 1      # '*' as '('

            if high < 0:
                return False

            if low < 0:
                low = 0

        return low == 0


        #O(n^2),O(n^2)
        # n = len(s)

        # dp = [[False] * (n + 1) for _ in range(n + 1)]

        # dp[0][0] = True

        # for i in range(n):
        #     for open_count in range(n + 1):

        #         if not dp[i][open_count]:
        #             continue

        #         if s[i] == '(':
        #             dp[i + 1][open_count + 1] = True

        #         elif s[i] == ')':
        #             if open_count > 0:
        #                 dp[i + 1][open_count - 1] = True

        #         else:
        #             # '*' as '('
        #             dp[i + 1][open_count + 1] = True

        #             # '*' as ')'
        #             if open_count > 0:
        #                 dp[i + 1][open_count - 1] = True

        #             # '*' as empty
        #             dp[i + 1][open_count] = True

        # return dp[n][0]


        #O(n),O(1)
        # balance = 0

        # # Left → Right
        # for ch in s:
        #     if ch == '(' or ch == '*':
        #         balance += 1
        #     else:
        #         balance -= 1

        #     if balance < 0:
        #         return False

        # balance = 0

        # # Right → Left
        # for ch in reversed(s):
        #     if ch == ')' or ch == '*':
        #         balance += 1
        #     else:
        #         balance -= 1

        #     if balance < 0:
        #         return False

        # return True