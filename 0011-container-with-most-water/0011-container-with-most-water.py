class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        r = n-1
        l =0 
        while(l<r):
            a = (r-l)*min(height[l],height[r])
            res = max(a,res)
            
            if(height[r]>height[l]):
                l += 1
            else:
                r -=1
        return res