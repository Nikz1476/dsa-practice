class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Brute Force - O(n^2), O(n)
        # if len(s) != len(t):
        #     return False

        # t = list(t)

        # for ch in s:
        #     found = False

        #     for i in range(len(t)):
        #         if t[i] == ch:
        #             t[i] = "#"      # mark as used
        #             found = True
        #             break

        #     if not found:
        #         return False

        # return True


        #sorting - O(nlogn)
        # if len(s) != len(t):
        #     return False

        # return sorted(s) == sorted(t)


        if len(s) != len(t):
            return False

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:

            if ch not in freq:
                return False

            freq[ch] -= 1

            if freq[ch] < 0:
                return False

        return True