class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #recursion - O(n),O(n)
        # def helper(left, right):
        #     if left >= right:
        #         return

        #     s[left], s[right] = s[right], s[left]
        #     helper(left + 1, right - 1)

        # helper(0, len(s) - 1)

        #stack - O(n),O(n)
        # stack = []

        # for ch in s:
        #     stack.append(ch)

        # for i in range(len(s)):
        #     s[i] = stack.pop()

        #built in python function - O(n),O(1)
        # s.reverse()

        #slicing - not in place - O(n),O(n)
        # s[:] = s[::-1]


        #optimal - O(n), O(1)
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1