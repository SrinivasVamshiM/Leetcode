class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 =[]
        ans2 = []
        totalans = []
        n = len(nums1)
        m = len(nums2)
        for i in range(n):
            if nums1[i] not in nums2 and nums1[i] not in ans1:
                ans1.append(nums1[i])
        for j in range(m):
            if nums2[j] not in nums1 and nums2[j] not in ans2:
                ans2.append(nums2[j])
        totalans.append(ans1)
        totalans.append(ans2)
        return totalans