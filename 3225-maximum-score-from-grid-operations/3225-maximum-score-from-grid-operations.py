class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0

        H = n + 1
        NEG = -10**30

        pref = [[0] * (n + 1) for _ in range(n)]
        for c in range(n):
            for r in range(n):
                pref[c][r + 1] = pref[c][r] + grid[r][c]

        def score(c, h, left, right):
            mx = max(left, right)
            if mx <= h:
                return 0
            return pref[c][mx] - pref[c][h]

        dp = [[NEG] * H for _ in range(H)]

        for h0 in range(H):
            for h1 in range(H):
                dp[h0][h1] = score(0, h0, 0, h1)

        for c in range(1, n - 1):
            ndp = [[NEG] * H for _ in range(H)]

            for cur in range(H):
                base = [dp[left][cur] for left in range(H)]

                pref_best = [NEG] * H
                best = NEG
                for left in range(H):
                    best = max(best, base[left])
                    pref_best[left] = best

                suff_best = [NEG] * (H + 1)
                best = NEG
                for left in range(H - 1, -1, -1):
                    gain = pref[c][left] - pref[c][cur] if left > cur else 0
                    best = max(best, base[left] + gain)
                    suff_best[left] = best

                for right in range(H):
                    gain_right = pref[c][right] - pref[c][cur] if right > cur else 0

                    val1 = pref_best[right] + gain_right
                    val2 = suff_best[right + 1]

                    ndp[cur][right] = max(val1, val2)

            dp = ndp

        ans = 0
        last = n - 1

        for left in range(H):
            for cur in range(H):
                ans = max(ans, dp[left][cur] + score(last, cur, left, 0))

        return ans