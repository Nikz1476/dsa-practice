class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # target = sorted(s1)
        # n = len(s1)

        # for i in range(len(s2) - n + 1):
        #     window = sorted(s2[i:i+n])

        #     if window == target:
        #         return True

        # return False

        target = Counter(s1)
        n = len(s1)

        for i in range(len(s2) - n + 1):
            window = Counter(s2[i:i+n])

            if window == target:
                return True

        return False


        # if len(s1) > len(s2):
        #     return False

        # count = [0] * 26

        # for c in s1:
        #     count[ord(c) - ord('a')] += 1

        # for i in range(len(s1)):
        #     count[ord(s2[i]) - ord('a')] -= 1

        # if all(x == 0 for x in count):
        #     return True

        # for i in range(len(s1), len(s2)):

        #     # Add the new character
        #     count[ord(s2[i]) - ord('a')] -= 1

        #     # Remove the character leaving the window
        #     count[ord(s2[i - len(s1)]) - ord('a')] += 1

        #     if all(x == 0 for x in count):
        #         return True

        # return False