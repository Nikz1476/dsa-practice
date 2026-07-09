class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #brute force - O(m*n),O(1)
        # for row in matrix:
        #     for num in row:
        #         if num == target:
        #             return True
        # return False


        #better - O(logm + logn), O(1)
        # rows = len(matrix)
        # cols = len(matrix[0])

        # # Binary search on rows
        # low = 0
        # high = rows - 1

        # while low <= high:
        #     mid = (low + high) // 2

        #     if target < matrix[mid][0]:
        #         high = mid - 1
        #     elif target > matrix[mid][cols - 1]:
        #         low = mid + 1
        #     else:
        #         # Target can only be in this row

        #         left = 0
        #         right = cols - 1

        #         while left <= right:
        #             m = (left + right) // 2

        #             if matrix[mid][m] == target:
        #                 return True
        #             elif matrix[mid][m] < target:
        #                 left = m + 1
        #             else:
        #                 right = m - 1

        #         return False

        # return False


        #optimal - O(logn), O(1)
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2

            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False