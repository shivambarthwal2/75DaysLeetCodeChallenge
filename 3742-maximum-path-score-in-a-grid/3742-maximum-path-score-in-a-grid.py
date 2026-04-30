class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for cost in range(k + 1):
                    if dp[i][j][cost] == -1:
                        continue

                    for ni, nj in [(i + 1, j), (i, j + 1)]:
                        if ni < m and nj < n:
                            val = grid[ni][nj]
                            add_score = val
                            add_cost = 1 if val in (1, 2) else 0

                            new_cost = cost + add_cost

                            if new_cost <= k:
                                dp[ni][nj][new_cost] = max(
                                    dp[ni][nj][new_cost],
                                    dp[i][j][cost] + add_score
                                )

        ans = max(dp[m - 1][n - 1])
        return ans if ans != -1 else -1