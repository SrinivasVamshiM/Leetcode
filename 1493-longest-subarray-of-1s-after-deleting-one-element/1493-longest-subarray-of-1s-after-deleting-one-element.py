class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = maxsum = 0
        numlen = len(nums)
        k = 1
        if len(nums) == 1:
            return 0
        
        
        for r,num in enumerate(nums):
            k -= 1 - num
            
            if k < 0:
                k += 1 - nums[l]
                l += 1
            else:
                maxsum = max(maxsum, r-l)
        return maxsum