class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        ops = 0
        seen = set()
        
        for i in c:
            if i not in seen and (k-i) in c:
                if i == (k-i):
                    ops += c[i] // 2
                else:
                    ops += min(c[i], c[k-i])
                seen.add(i)
                seen.add(k-i)
        return ops
                    