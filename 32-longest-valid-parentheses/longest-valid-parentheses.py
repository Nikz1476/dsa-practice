class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # # brute force, time - O(n^3), space - O(1)
        # def isValid(sub):
        #     count = 0
        #     for ch in sub:
        #         if ch == '(':
        #             count += 1
        #         else:
        #             count -= 1
        #         if count < 0:
        #             return False
        #     return count == 0

        # n = len(s)
        # max_len = 0

        # for i in range(n):
        #     for j in range(i + 1, n + 1):
        #         if isValid(s[i:j]):
        #             max_len = max(max_len, j - i)

        # return max_len


        # # better - stack , time and space - O(n)
        # stack = [-1]
        # max_len = 0

        # for i in range(len(s)):
        #     if s[i] == '(':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if not stack:
        #             stack.append(i)
        #         else:
        #             max_len = max(max_len, i - stack[-1])

        # return max_len


        # # optimal, time - (n), space - O(1)
    #     left = right = 0
    #     max_len = 0

    # # Left to right
    #     for ch in s:
    #         if ch == '(':
    #             left += 1
    #         else:
    #             right += 1

    #         if left == right:
    #             max_len = max(max_len, 2 * right)
    #         elif right > left:
    #             left = right = 0

    # # Right to left
    #     left = right = 0
    #     for ch in reversed(s):
    #         if ch == '(':
    #             left += 1
    #         else:
    #             right += 1

    #         if left == right:
    #             max_len = max(max_len, 2 * left)
    #         elif left > right:
    #             left = right = 0

    #     return max_len

        # # better - dp, time and space - O(n)
        n = len(s)
        dp = [0] * n
        max_len = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                else:
                    prev = i - dp[i-1] - 1
                    if prev >= 0 and s[prev] == '(':
                        dp[i] = dp[i-1] + 2
                        if prev - 1 >= 0:
                            dp[i] += dp[prev - 1]

            max_len = max(max_len, dp[i])

        return max_len