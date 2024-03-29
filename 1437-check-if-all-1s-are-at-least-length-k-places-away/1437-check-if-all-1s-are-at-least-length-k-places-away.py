class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        list1 = []
        for i,j in enumerate(nums):
            if j == 1:
                list1.append(i)
        n = len(list1)
        print(list1)
        for l in range(n-1):
            if(list1[l+1]-list1[l] < k+1):
                return False
        return True