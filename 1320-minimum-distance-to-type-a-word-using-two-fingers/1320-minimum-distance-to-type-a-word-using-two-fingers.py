class Solution:
    def minimumDistance(self, word: str) -> int:
        from functools import lru_cache

        def dist(a, b):
            if a is None or b is None:
                return 0
            x1, y1 = divmod(a, 6)
            x2, y2 = divmod(b, 6)
            return abs(x1 - x2) + abs(y1 - y2)

        @lru_cache(None)
        def dp(i, f1, f2):
            if i == len(word):
                return 0

            curr = ord(word[i]) - ord('A')

            use_f1 = dist(f1, curr) + dp(i + 1, curr, f2)

            use_f2 = dist(f2, curr) + dp(i + 1, f1, curr)

            return min(use_f1, use_f2)

        return dp(0, None, None)