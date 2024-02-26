class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        out = []
        if n < 2:
            return out
        for i in range(0, n-1):
            c = 0
            for j in range(i+1, n):
                c = nums[i] + nums[j] 
                if c == target:
                    out.append(i)
                    out.append(j)
                    return out
        return out