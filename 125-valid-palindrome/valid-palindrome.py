class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # O(n), O(n)
        # cleaned = ""
        # for ch in s:
        #     if ch.isalnum():
        #         cleaned += ch.lower()

        # return cleaned == cleaned[::-1]

        # #O(n),O(n)
        # t = ''.join(c.lower() for c in s if c.isalnum())
        # return t == t[::-1]

        #O(n),O(1)
        l = 0
        r = len(s) - 1

        while l < r:

            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True