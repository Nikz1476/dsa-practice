class Solution:
    def isValid(self, s: str) -> bool:
        #brute force, time - O(n^2), space - O(n)
        # prev = None
        # while prev != s:
        #     prev = s
        #     s = s.replace("()", "").replace("{}", "").replace("[]", "")
        # return s == ""

        #better - stack explicit mapping
        # stack = []
        # mapping = {')': '(', '}': '{', ']': '['}

        # for char in s:
        #     if char in mapping.values():   # opening bracket
        #         stack.append(char)
        #     else:  # closing bracket
        #         if not stack or stack[-1] != mapping[char]:
        #             return False
        #         stack.pop()

        # return not stack

        #optimal, time and space - O(n) both this and above method.
        stack = []

        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            else:
                if not stack or stack.pop() != c:
                    return False

        return not stack
