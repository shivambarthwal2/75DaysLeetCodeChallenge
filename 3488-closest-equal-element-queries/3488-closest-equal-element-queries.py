class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from collections import defaultdict
        import bisect
        
        n = len(nums)
        pos = defaultdict(list)
        
        # map value -> indices
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        res = []
        
        for q in queries:
            val = nums[q]
            indices = pos[val]
            
            if len(indices) == 1:
                res.append(-1)
                continue
            
            idx = bisect.bisect_left(indices, q)
            ans = float('inf')
            
            # check left neighbor
            if idx > 0:
                j = indices[idx - 1]
                diff = abs(q - j)
                ans = min(ans, min(diff, n - diff))
            
            # check right neighbor
            if idx < len(indices) - 1:
                j = indices[idx + 1]
                diff = abs(q - j)
                ans = min(ans, min(diff, n - diff))
            
            # circular wrap (first & last)
            j = indices[0]
            if j != q:
                diff = abs(q - j)
                ans = min(ans, min(diff, n - diff))
            
            j = indices[-1]
            if j != q:
                diff = abs(q - j)
                ans = min(ans, min(diff, n - diff))
            
            res.append(ans)
        
        return res