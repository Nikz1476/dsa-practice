class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        #O(mn),O(mn)
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0

            val = grid[r][c]
            grid[r][c] = 0  # Mark visited

            val += dfs(r + 1, c)
            val += dfs(r - 1, c)
            val += dfs(r, c + 1)
            val += dfs(r, c - 1)

            return val

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    total = dfs(i, j)
                    if total % k == 0:
                        count += 1

        return count


        # m, n = len(grid), len(grid[0])
        # count = 0

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] > 0:
        #             q = deque([(i, j)])
        #             total = 0
        #             total += grid[i][j]
        #             grid[i][j] = 0

        #             while q:
        #                 r, c = q.popleft()

        #                 for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        #                     nr, nc = r + dr, c + dc

        #                     if (0 <= nr < m and 0 <= nc < n
        #                             and grid[nr][nc] > 0):
        #                         total += grid[nr][nc]
        #                         grid[nr][nc] = 0
        #                         q.append((nr, nc))

        #             if total % k == 0:
        #                 count += 1

        # return count