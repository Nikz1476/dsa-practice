from itertools import permutations

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # ans = None

        # for p in permutations(s):
        #     curr = ''.join(p)

        #     if curr > target:
        #         if ans is None or curr < ans:
        #             ans = curr

        # if ans is None:
        #     return ""

        # return ans

        n = len(s)
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - 97] += 1

        def solve(i, greater):
            if i == n:
                return "" if greater else None

            x = ord(target[i]) - 97

            # Try characters in sorted order
            for j in range(26):
                if cnt[j] == 0:
                    continue

                if not greater and j < x:
                    continue

                if not greater and j == x:
                    cnt[j] -= 1
                    r = solve(i + 1, False)
                    cnt[j] += 1
                else:
                    cnt[j] -= 1
                    r = solve(i + 1, True)
                    cnt[j] += 1

                if r is not None:
                    return chr(j + 97) + r

            return None

        ans = solve(0, False)
        return "" if ans is None else ans