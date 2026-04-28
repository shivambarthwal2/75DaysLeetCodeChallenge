class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []

        for row in grid:
            for val in row:
                arr.append(val)

        rem = arr[0] % x

        for val in arr:
            if val % x != rem:
                return -1

        arr.sort()
        median = arr[len(arr) // 2]

        ops = 0

        for val in arr:
            ops += abs(val - median) // x

        return ops