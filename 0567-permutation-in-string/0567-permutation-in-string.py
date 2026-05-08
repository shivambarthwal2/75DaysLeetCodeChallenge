class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        count1 = Counter(s1)
        window = Counter(s2[:n1])

        if count1 == window:
            return True

        left = 0

        for right in range(n1, n2):
            window[s2[right]] += 1

            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1

            if window == count1:
                return True

        return False