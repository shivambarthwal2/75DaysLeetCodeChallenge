class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        directions = {
            1: [(0, -1), (0, 1)],     
            2: [(-1, 0), (1, 0)],     
            3: [(0, -1), (1, 0)],     
            4: [(0, 1), (1, 0)],      
            5: [(0, -1), (-1, 0)],    
            6: [(0, 1), (-1, 0)]      
        }

        visited = set()

        def dfs(r, c):
            if (r, c) == (m - 1, n - 1):
                return True

            visited.add((r, c))

            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if (nr, nc) in visited:
                    continue

                if (-dr, -dc) in directions[grid[nr][nc]]:
                    if dfs(nr, nc):
                        return True

            return False

        return dfs(0, 0)