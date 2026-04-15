class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = float('inf')

        for i in range(n):
            if words[i] == target:
                diff = abs(i - startIndex)
                dist = min(diff, n - diff)
                ans = min(ans, dist)

        return ans if ans != float('inf') else -1