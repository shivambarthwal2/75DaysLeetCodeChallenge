class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        import bisect
        
        def get_pos(x, y):
            if x == 0:
                return y
            elif y == side:
                return side + x
            elif x == side:
                return 3 * side - y
            else:
                return 4 * side - x
        
        arr = sorted(get_pos(x, y) for x, y in points)
        n = len(arr)
        perimeter = 4 * side
        
        def can(d):
            extended = arr + [x + perimeter for x in arr]
            
            for start in range(n):
                count = 1
                cur = extended[start]
                idx = start
                limit = arr[start] + perimeter - d
                
                while count < k:
                    idx = bisect.bisect_left(extended, cur + d, idx + 1)
                    
                    if idx >= start + n or extended[idx] > limit:
                        break
                    
                    cur = extended[idx]
                    count += 1
                
                if count == k:
                    return True
            
            return False
        
        left, right = 0, side
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans