class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = maxnum = 0
        for r,num in enumerate(nums):
            k -= 1-num
            
            if k< 0 :
                k += 1 - nums[l]
                l += 1
            else:
                maxnum = max(maxnum, r-l+1)
        return maxnum
                