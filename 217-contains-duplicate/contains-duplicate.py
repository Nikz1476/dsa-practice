from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        freqcount = defaultdict(int)

        for x in nums:
            freqcount[x] = freqcount.get(x,0) + 1
        
        for value in freqcount.values():
            if value > 1:
                return True
        return False