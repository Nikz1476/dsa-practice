class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #O(n^2),O(1)
        # n = len(fruits)
        # ans = 0
        # for i in range(n):
        #     basket = set()
        #     for j in range(i,n):
        #         basket.add(fruits[j])
        #         if len(basket) > 2:
        #             break
        #         ans = max(ans,j-i+1)
        # return ans         

        start = 0
        end = len(fruits)
        maxlen = 0
        fruitcount = {}
        for i in range(end):
            if fruits[i] not in fruitcount:
                fruitcount[fruits[i]] = 1
            else:
                fruitcount[fruits[i]]+=1
            while len(fruitcount) > 2:
                fruitcount[fruits[start]] -= 1

                if fruitcount[fruits[start]] == 0:
                    del fruitcount[fruits[start]]

                start += 1
            maxlen = max(maxlen,i-start+1)
        return maxlen

