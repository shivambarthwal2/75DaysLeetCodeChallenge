class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def withinTwoEdits(a, b):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
                    if diff > 2:
                        return False
            return True
        
        res = []
        
        for q in queries:
            for d in dictionary:
                if withinTwoEdits(q, d):
                    res.append(q)
                    break
        
        return res