class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        from functools import lru_cache
        
        robot.sort()
        factory.sort()
        
        n = len(robot)
        m = len(factory)

        @lru_cache(None)
        def dp(i, j):
        
            if i == n:
                return 0
            
  
            if j == m:
                return float('inf')
            
            res = dp(i, j + 1) 
            
            pos, limit = factory[j]
            dist = 0
            
            
            for k in range(1, limit + 1):
                if i + k - 1 >= n:
                    break
                
                dist += abs(robot[i + k - 1] - pos)
                res = min(res, dist + dp(i + k, j + 1))
            
            return res
        
        return dp(0, 0)