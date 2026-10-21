class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        # 1. Check if s is already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
        
        min_char = min(s)
        max_char = max(s)
        
        # 2. operation is enough if s[0] is min or s[-1] is max
        if s[0] == min_char or s[-1] == max_char:
            return 1
        
        # 3. If length < 3 and not sorted, impossible
        if n < 3:
            return -1
        
        # 4. 3 operations needed ONLY if s[0] is the UNIQUE max AND s[-1] is the UNIQUE min
        if s[0] == max_char and s.count(max_char) == 1 and s[-1] == min_char and s.count(min_char) == 1:
            return 3
            
        # 5. Otherwise, 2 operations are sufficient
        return 2