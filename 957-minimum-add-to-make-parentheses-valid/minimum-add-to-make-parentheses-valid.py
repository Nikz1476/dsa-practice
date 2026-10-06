class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        #O(n),O(1)
        balance = 0
        ans = 0

        for ch in s:
            if ch == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    ans += 1

        return ans + balance


        #O(n),O(n)
        # stack = []

        # for ch in s:
        #     if ch == '(':
        #         stack.append(ch)
        #     else:
        #         if len(stack) > 0:
        #             stack.pop()
        #         else:
        #             stack.append(')')

        # return len(stack)