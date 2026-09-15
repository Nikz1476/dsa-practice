class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        #Brute Force - time - O(900 * 10) = O(1), space - O(10) = O(1)
        # freq = [0] * 10
        # for d in digits:
        #     freq[d] += 1

        # ans = 0
        # for num in range(100, 1000):
        #     if num % 2 != 0:
        #         continue

        #     a = num // 100
        #     b = (num // 10) % 10
        #     c = num % 10

        #     # Check if we have enough copies
        #     needed = [0] * 10
        #     needed[a] += 1
        #     needed[b] += 1
        #     needed[c] += 1

        #     valid = True

        #     for d in range(10):
        #         if needed[d] > freq[d]:
        #             valid = False
        #             break

        #     if valid:
        #         ans += 1

        # return ans

        #Better solution  - O(9*10*5) = O(1)
        # freq = [0] * 10
        # for d in digits:
        #     freq[d] +=1
        # ans = 0
        # for a in range (1,10):
        #     if freq[a] == 0:
        #         continue
        #     freq[a]-=1
        #     for b in range(0,10):
        #         if freq[b] == 0:
        #             continue
        #         freq[b]-=1
        #         for c in range(0,10,2):
        #             if freq[c] > 0:
        #                 ans+=1
        #         freq[b]+=1
        #     freq[a]+=1
        # return ans

        #O(n^3),O(1) - auxiliary
        ans = set()
        n = len(digits)
        for i in range(n):
            if digits[i] == 0:
                continue

            for j in range(n):
                if j == i:
                    continue

                for k in range(n):
                    if k == i or k == j:
                        continue

                    if digits[k] % 2 != 0:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]

                    ans.add(num)

        return len(ans)