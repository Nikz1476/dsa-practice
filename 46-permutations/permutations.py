class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #O(n*n!) - time and space
        # res = []
        # for p in permutations(nums):
        #     res.append(p)
        # return res


        #recursive without used[]
        #time - O(n*n!) , space - auxiliary - O(n)
        if len(nums) == 1:
            return [nums]
        result = []

        for i in range(len(nums)):
            current = nums[i]
            remaining = nums[:i] + nums[i+1:]
            for p in self.permute(remaining):
                result.append([current]+p)
        return result


        # result = []

        # def dfs(path, used):

        #     if len(path) == len(nums):
        #         result.append(path[:])
        #         return

        #     for i in range(len(nums)):

        #         if used[i]:
        #             continue

        #         used[i] = True
        #         path.append(nums[i])

        #         dfs(path, used)

        #         path.pop()
        #         used[i] = False

        # dfs([], [False] * len(nums))

        # return result

