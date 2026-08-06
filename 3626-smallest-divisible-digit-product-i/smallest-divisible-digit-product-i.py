class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,101):
            x =i
            prod =1

            while x > 0:
                prod = prod * (x%10)
                x//=10

            if prod % t == 0:
                return i