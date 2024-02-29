class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numsc = nums1+nums2
        numsc.sort()
        m = len(numsc)
        n = 0.0
        print(numsc)
        if m%2 == 0:
            k = m//2
            n = (numsc[k]+numsc[k-1])/2
        else:
            k = m//2
            n = numsc[k]
        return n